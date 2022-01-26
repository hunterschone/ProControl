# !/bin/bash
#%
#% Inflates individual brains, runs inter-hemispheric cortical surface-based registration
#% (left hemisphere registered to right hemisphere), resamples Joern's ROIs to the individual's
#% surfaces and projects the ROIs back onto individual's volume. Requires T1w images
#% registered to midspace.
#%
#% Created by Paulina Kieliba, 2019
#%
#=======================================================================================
#% USAGE
#% fsPipeline [-h] [subject code]
#%
#% EXAMPLE
#% fsPipeline SF2
#%
#=======================================================================================
# END_OF_HEADER
#=======================================================================================

# Printing help function
function usage() {
  HEADSIZE=$(head -200 "${0}" | grep -n "^# END_OF_HEADER" | cut -f1 -d:)
  head -"${HEADSIZE}" "${0}" | grep -e "^#%" | sed -e "s/^#%//g"
  exit 0
}

[[ $1 == "-h" ]] && usage && exit 1
[ $# -lt 1 ] && usage && exit 1

module add freesurfer
surfDir=/misc/data19/schonehr/ProControl/data/DONE/
export SUBJECTS_DIR="${surfDir}"
subj="$1"

# check whether subj dir exists, if not create it
if [ ! -d "${SUBJECTS_DIR}"/"${subj}" ]; then
    sessions=`ls -d /misc/data19/schonehr/ProControl/data/DONE/"${subj}"/[p]*`  # assumes that names of all scanning sessions start with "p", e.g. pre, post, postpost
    sesArray=(${sessions//\\n/})
    # create subj dir
    if [ ${#sesArray[@]} -eq 3 ]; then
        recon-all -i "${sesArray[0]}"/anat/*T1w_to_midsp.nii.gz -i "${sesArray[1]}"/anat/*T1w_to_midsp.nii.gz -i "${sesArray[2]}"/anat/*T1w_to_midsp.nii.gz -s "${subj}"
    elif [ ${#sesArray[@]} -eq 2 ]; then
        recon-all -i "${sesArray[0]}"/anat/*T1w_to_midsp.nii.gz -i "${sesArray[1]}"/anat/*T1w_to_midsp.nii.gz -s "${subj}"
    fi
fi

# check if recon-all has been run, if not run it
if [ ! -f "${SUBJECTS_DIR}"/"${subj}"/surf/lh.pial ]; then
    reconID=`fsl_sub -q verylong.q recon-all -all -s "${subj}"` # run recon-all
    fsl_sub -q short.q -j $reconID mri_convert "${surfDir}"/"${subj}"/mri/T1.mgz "${surfDir}"/"${subj}"/mri/T1.nii.gz
    # create giftis
    giftiID=`fsl_sub -q short.q -j $reconID /misc/data19/schonehr/ProControl/scripts/freesurfer/fsCreateGifti.sh "${subj}" "${surfDir}"/"${subj}"/gifti`
    # resample atlas into LHemi
    resampID=`fsl_sub -q short.q -j $giftiID /misc/data19/schonehr/ProControl/scripts/freesurfer/fsSurf2Surf.sh "${subj}" /misc/data19/schonehr/ProControl/model/masks/Joern /misc/data19/schonehr/ProControl/model/masks/Joern/ROI.label.gii L "${surfDir}"/"${subj}"/gifti`
    # project surf L.ROI to volume
    projID=`fsl_sub -q short.q -j $resampID /misc/data19/schonehr/ProControl/scripts/freesurfer/fsSurfProjBackL.sh "${subj}" L "${surfDir}"/"${subj}"/gifti/ROI/"${subj}".ROI.L.label.gii`
    # coregister hemispheres
    echo "/vols/Data/soma/6Finger/scripts/exec-matlab-Xhemi.sh "${subj}"" > /misc/data19/schonehr/ProControl/scripts/freesurfer/logs/Xhem"${subj}"
    xhemID=$(/misc/data19/schonehr/ProControl/scripts/freesurfer/submit-matlab.sh /misc/data19/schonehr/ProControl/scripts/freesurfer/logs/Xhem"${subj}" long.q Xhemi $reconID)
    # resample atlas into RHemi
    resampXhemID=`fsl_sub -q short.q -j "${xhemID}","${resampID}" /misc/data19/schonehr/ProControl/scripts/freesurfer/fsXhemi.sh "${subj}" "${surfDir}"/"${subj}"/gifti/ROI/"${subj}".ROI.L.label.gii lr`
    # project surf R.ROI to volume
    fsl_sub -q short.q -j $resampXhemID /misc/data19/schonehr/ProControl/scripts/freesurfer/fsSurfProjBackL.sh "${subj}" R "${surfDir}"/"${subj}"/gifti/ROI/"${subj}".ROI.R.label.gii
else
    # check if gifti has been created, if not create it
    if [ ! -f "${SUBJECTS_DIR}"/"${subj}"/gifti/"${subj}".L.midthickness.surf.gii ]; then
      # create giftis
      giftiID=`fsl_sub -q short.q /misc/data19/schonehr/ProControl/scripts/freesurfer/fsCreateGifti.sh "${subj}" "${surfDir}"/"${subj}"/gifti`
      # resample atlas into LHemi
      resampID=`fsl_sub -q short.q -j $giftiID /misc/data19/schonehr/ProControl/scripts/freesurfer/fsSurf2Surf.sh "${subj}" /misc/data19/schonehr/ProControl/model/masks/Joern /misc/data19/schonehr/ProControl/model/masks/Joern/ROI.label.gii L "${surfDir}"/"${subj}"/gifti`
      # project surf ROI to volume
      projID=`fsl_sub -q short.q -j $resampID /misc/data19/schonehr/ProControl/scripts/freesurfer/fsSurfProjBackL.sh "${subj}" L "${surfDir}"/"${subj}"/gifti/ROI/"${subj}".ROI.L.label.gii`
    else
        # check if atlas has been resampled
        if [ ! -f "${SUBJECTS_DIR}"/"${subj}"/gifti/ROI/"${subj}".ROI.L.label.gii ]; then
            resampID=`fsl_sub -q short.q /misc/data19/schonehr/ProControl/scripts/freesurfer/fsSurf2Surf.sh "${subj}" /misc/data19/schonehr/ProControl/model/masks/Joern /misc/data19/schonehr/ProControl/model/masks/Joern//ROI.label.gii L "${surfDir}"/"${subj}"/gifti`
            # project surf ROI to volume
            projID=`fsl_sub -q short.q -j $resampID /misc/data19/schonehr/ProControl/scripts/freesurfer/fsSurfProjBackL.sh "${subj}" L "${surfDir}"/"${subj}"/gifti/ROI/"${subj}".ROI.L.label.gii`
        else
            # check if ROI projected to Volume
            if [ ! -d "${SUBJECTS_DIR}"/"${subj}"/gifti/Volume ]; then
                 fsl_sub -q short.q /misc/data19/schonehr/ProControl/scripts/freesurfer/fsSurfProjBackL.sh "${subj}" L "${surfDir}"/"${subj}"/gifti/ROI/"${subj}".ROI.L.label.gii
            fi
        fi
    fi

    sleep 2

    # check whether Xhemi has been created for the R hemisphere
    if [ ! -d "${SUBJECTS_DIR}"/"${subj}"/xhemi ]; then
        echo "/vols/Data/soma/6Finger/scripts/exec-matlab-Xhemi.sh "${subj}"" > /vols/Data/soma/6Finger/scripts/logs/Xhem"${subj}"
        xhemID=$(/vols/Data/soma/6Finger/scripts/submit-matlab.sh /vols/Data/soma/6Finger/scripts/logs/Xhem"${subj}" long.q Xhemi)
        # resample atlas into RHemi
        resampXhemID=`fsl_sub -q short.q -j $xhemID /vols/Data/soma/6Finger/scripts/fsXhemi.sh "${subj}" "${surfDir}"/"${subj}"/gifti/ROI/"${subj}".ROI.L.label.gii lr`
        fsl_sub -q short.q -j $resampXhemID /vols/Data/soma/6Finger/scripts/fsSurfProjBackL.sh "${subj}" R "${surfDir}"/"${subj}"/gifti/ROI/${subj}.ROI.R.label.gii
    else
      if [[ -f "${SUBJECTS_DIR}"/"${subj}"/gifti/"${subj}".ROI.R.label.gii ]]; then
        # resamplw atlas into RHemi
        resampXhemID=`fsl_sub -q short.q /vols/Data/soma/6Finger/scripts/fsXhemi.sh "${subj}" "${surfDir}"/"${subj}"/gifti/ROI/"${subj}".ROI.L.label.gii lr`
        fsl_sub -q short.q -j $resampXhemID /vols/Data/soma/6Finger/scripts/fsSurfProjBackL.sh "${subj}" R "${surfDir}"/"${subj}"/gifti/ROI/"${subj}".ROI.R.label.gii
      else
        resampXhemID=`fsl_sub -q short.q  -j $resampID /vols/Data/soma/6Finger/scripts/fsXhemi.sh "${subj}" "${surfDir}"/"${subj}"/gifti/ROI/"${subj}".ROI.L.label.gii lr`
        fsl_sub -q short.q -j $resampXhemID /vols/Data/soma/6Finger/scripts/fsSurfProjBackL.sh "${subj}" R "${surfDir}"/"${subj}"/gifti/ROI/"${subj}".ROI.R.label.gii
      fi
    fi
fi
