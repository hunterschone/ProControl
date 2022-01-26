
# !/bin/bash

# This script inflates individual brains, registers both hemispheres together, register Joern's atlas to the existing surfaces and project the ROIs back onto the volume.
# Created by Paulina Kieliba, 2019
# Adapted by Dollyane Muret, 2021

surfDir=/vols/Data/soma/Adapticity/data/freesurfer
SUBJECTS_DIR=$surfDir
subj=$1 #AD_CT01
ROI_LH=$2
ROI_RH=$3


# check if recon-all has been run, if not run it
if [ ! -e $SUBJECTS_DIR/$subj/surf/lh.pial ]; then #checks if freesurfer folder exists
    reconID=`fsl_sub -q verylong.q recon-all -i /vols/Data/soma/Adapticity/data/${subj}/anat/${subj}_T1w.nii.gz -subjid ${subj} -all` # run recon-all
    #reconID=`fsl_sub -q verylong.q recon-all -i -all -s $subj` # run recon-all
    fsl_sub -q short.q -j $reconID mri_convert $surfDir/$subj/mri/T1.mgz $surfDir/$subj/mri/T1.nii.gz
    # create giftis
    giftiID=`fsl_sub -q short.q -j $reconID /vols/Data/soma/Adapticity/scripts/Face_scripts/fsCreateGifti.sh $subj $surfDir/$subj/gifti $surfDir/$subj`
    # resample atlas into LHemi
    resampID=`fsl_sub -q short.q -j $giftiID /vols/Data/soma/Adapticity/scripts/Face_scripts/fsSurf2Surf.sh $subj /vols/Data/soma/Atlases/Joern /vols/Data/soma/Atlases/Joern/${ROI_LH}.label.gii 0 $surfDir/$subj/gifti $surfDir/$subj target`
    # project surf L.ROI to volume
    projID=`fsl_sub -q short.q -j $resampID /vols/Data/soma/Adapticity/scripts/Face_scripts/fsSurfProjBackL.sh $subj $surfDir/$subj/gifti 0 $surfDir/$subj/gifti/ROI/${subj}.${ROI_LH}.L.label.gii ${ROI_LH}`
    # coregister hemispheres
    echo "/vols/Data/soma/Adapticity/scripts/Face_scripts/exec-matlab-Xhemi.sh $subj" > /vols/Data/soma/Adapticity/scripts/Face_scripts/logs/Xhem${subj}#allows you to submit matlab scripts to queue
    xhemID=$(/vols/Data/soma/Adapticity/scripts/Face_scripts/submit-matlab.sh /vols/Data/soma/Adapticity/scripts/Face_scripts/logs/Xhem$subj long.q Xhemi $reconID)
    # create giftis from xhemi files
    giftiXhemID=`fsl_sub -q long.q -j $xhemID /vols/Data/soma/Adapticity/scripts/Face_scripts/wb_shortcuts -freesurfer-resample-prep $surfDir/$subj/xhemi/surf/lh.white $surfDir/$subj/xhemi/surf/lh.pial $surfDir/$subj/xhemi/surf/lh.fsaverage_sym.sphere.reg /vols/Data/soma/Atlases/Joern/rh.sphere.reg.surf.gii $surfDir/$subj/gifti/lh.xhemimidthickness.surf.gii /vols/Data/soma/Atlases/Joern/R.midthickness.surf.gii $surfDir/$subj/gifti/lh.xhemisphere.reg.surf.gii`
    # resample atlas into RHemi
    resampXhemID=`fsl_sub -q long.q -j $giftiXhemID wb_command -label-resample /vols/Data/soma/Atlases/Joern/${ROI_RH}.label.gii /vols/Data/soma/Atlases/Joern/rh.SPHERE.REG.surf.gii $surfDir/${subj}/gifti/lh.xhemisphere.reg.surf.gii ADAP_BARY_AREA $surfDir/$subj/gifti/ROI/${subj}.${ROI_RH}.R.label.gii -area-surfs /vols/Data/soma/Atlases/Joern/rh.midthickness.surf.gii $surfDir/${subj}/gifti/lh.xhemimidthickness.surf.gii`
    # project surf R.ROI to volume
    fsl_sub -q short.q -j $resampXhemID /vols/Data/soma/Adapticity/scripts/Face_scripts/fsSurfProjBackL.sh $subj $surfDir/$subj/gifti 1 $surfDir/$subj/gifti/ROI/${subj}.${ROI_RH}.R.label.gii ${ROI_RH}
else
    # check if gifti has been created, if not create it
    if [ ! -e $SUBJECTS_DIR/$subj/gifti/${subj}.L.pial.surf.gii ]; then
        # create giftis
        giftiID=`fsl_sub -q short.q /vols/Data/soma/Adapticity/scripts/Face_scripts/fsCreateGifti.sh $subj $surfDir/$subj/gifti $surfDir/$subj`
        # resample atlas into LHemi
        resampID=`fsl_sub -q short.q -j $giftiID /vols/Data/soma/Adapticity/scripts/Face_scripts/fsSurf2Surf.sh $subj /vols/Data/soma/Atlases/Joern /vols/Data/soma/Atlases/Joern/${ROI_LH}.label.gii 0 $surfDir/$subj/gifti $surfDir/$subj target`
        # project surf ROI to volume
        projID=`fsl_sub -q short.q -j $resampID /vols/Data/soma/Adapticity/scripts/Face_scripts/fsSurfProjBackL.sh $subj $surfDir/$subj/gifti 0 $surfDir/$subj/gifti/ROI/${subj}.${ROI_LH}.L.label.gii ${ROI_LH}`
    else
        # check if atlas has been resampled
        if [ ! -e $SUBJECTS_DIR/$subj/gifti/ROI/${subj}.${ROI_LH}.L.label.gii ]; then
            resampID=`fsl_sub -q short.q /vols/Data/soma/Adapticity/scripts/Face_scripts/fsSurf2Surf.sh $subj /vols/Data/soma/Atlases/Joern /vols/Data/soma/Atlases/Joern/${ROI_LH}.label.gii 0 $surfDir/$subj/gifti $surfDir/$subj target`
            # project surf ROI to volume
            projID=`fsl_sub -q short.q -j $resampID /vols/Data/soma/Adapticity/scripts/Face_scripts/fsSurfProjBackL.sh $subj $surfDir/$subj/gifti 0 $surfDir/$subj/gifti/ROI/${subj}.${ROI_LH}.L.label.gii ${ROI_LH}`
        else
            # check if ROI projected to Volume
            if [ ! -e $SUBJECTS_DIR/$subj/gifti/Volume/${subj}_${ROI_LH}.ROI_lh_ribbon.nii.gz ]; then
                projID=`fsl_sub -q short.q /vols/Data/soma/Adapticity/scripts/Face_scripts/fsSurfProjBackL.sh $subj $surfDir/$subj/gifti 0 $surfDir/$subj/gifti/ROI/${subj}.${ROI_LH}.L.label.gii ${ROI_LH}`
            fi
        fi
    fi

    # check whether Xhemi has been created for the R hemisphere
    if [ ! -d $SUBJECTS_DIR/$subj/xhemi ]; then
        echo "/vols/Data/soma/Adapticity/scripts/Face_scripts/exec-matlab-Xhemi.sh $subj" > /vols/Data/soma/Adapticity/scripts/Face_scripts/logs/Xhem${subj}
        xhemID=$(/vols/Data/soma/Adapticity/scripts/Face_scripts/submit-matlab.sh /vols/Data/soma/Adapticity/scripts/Face_scripts/logs/Xhem$subj long.q Xhemi)
        # create giftis from xhemi files
        giftiXhemID=`fsl_sub -q long.q -j $xhemID /vols/Data/soma/Adapticity/scripts/Face_scripts/wb_shortcuts -freesurfer-resample-prep $surfDir/$subj/xhemi/surf/lh.white $surfDir/$subj/xhemi/surf/lh.pial $surfDir/$subj/xhemi/surf/lh.fsaverage_sym.sphere.reg /vols/Data/soma/Atlases/Joern/rh.sphere.reg.surf.gii $surfDir/$subj/gifti/lh.xhemimidthickness.surf.gii /vols/Data/soma/Atlases/Joern/R.midthickness.surf.gii $surfDir/$subj/gifti/lh.xhemisphere.reg.surf.gii`
        # resample atlas into RHemi
        resampXhemID=`fsl_sub -q long.q -j $giftiXhemID wb_command -label-resample /vols/Data/soma/Atlases/Joern/${ROI_RH}.label.gii /vols/Data/soma/Atlases/Joern/rh.SPHERE.REG.surf.gii $surfDir/${subj}/gifti/lh.xhemisphere.reg.surf.gii ADAP_BARY_AREA $surfDir/$subj/gifti/ROI/${subj}.${ROI_RH}.R.label.gii -area-surfs /vols/Data/soma/Atlases/Joern/rh.midthickness.surf.gii $surfDir/${subj}/gifti/lh.xhemimidthickness.surf.gii`
        # project surf R.ROI to volume
        fsl_sub -q short.q -j $resampXhemID /vols/Data/soma/Adapticity/scripts/Face_scripts/fsSurfProjBackL.sh $subj $surfDir/$subj/gifti 1 $surfDir/$subj/gifti/ROI/${subj}.${ROI_RH}.R.label.gii ${ROI_RH}
    #if [ ! -d $SUBJECTS_DIR/${subj}_adapt/xhemi ]; then
    #    echo "/vols/Data/soma/Adapticity/scripts/Face_scripts/exec-matlab-Xhemi.sh ${subj}_adapt" > /vols/Data/soma/Adapticity/scripts/Face_scripts/logs/Xhem${subj}_adapt
    #    xhemID=$(/vols/Data/soma/Adapticity/scripts/Face_scripts/submit-matlab.sh /vols/Data/soma/Adapticity/scripts/Face_scripts/logs/Xhem${subj}_adapt long.q Xhemi)
    #    # create giftis from xhemi files
    #    giftiXhemID=`fsl_sub -q long.q -j $xhemID /vols/Data/soma/Adapticity/scripts/Face_scripts/wb_shortcuts -freesurfer-resample-prep $surfDir/${subj}_adapt/xhemi/surf/lh.white $surfDir/${subj}_adapt/xhemi/surf/lh.pial $surfDir/${subj}_adapt/xhemi/surf/lh.fsaverage_sym.sphere.reg /vols/Data/soma/Atlases/Joern/rh.sphere.reg.surf.gii $surfDir/${subj}_adapt/gifti/lh.xhemimidthickness.surf.gii /vols/Data/soma/Atlases/Joern/R.midthickness.surf.gii $surfDir/${subj}_adapt/gifti/lh.xhemisphere.reg.surf.gii`
    else
        # check if xhemi gifti has been created, if not create it
        if [ ! -e $SUBJECTS_DIR/${subj}/gifti/lh.xhemisphere.reg.surf.gii ]; then
        #if [ ! -e $SUBJECTS_DIR/${subj}_adapt/gifti/lh.xhemisphere.reg.surf.gii ]; then
            # create giftis from xhemi files
            giftiXhemID=`fsl_sub -q long.q /vols/Data/soma/Adapticity/scripts/Face_scripts/wb_shortcuts -freesurfer-resample-prep $surfDir/$subj/xhemi/surf/lh.white $surfDir/$subj/xhemi/surf/lh.pial $surfDir/$subj/xhemi/surf/lh.fsaverage_sym.sphere.reg /vols/Data/soma/Atlases/Joern/rh.sphere.reg.surf.gii $surfDir/$subj/gifti/lh.xhemimidthickness.surf.gii /vols/Data/soma/Atlases/Joern/R.midthickness.surf.gii $surfDir/$subj/gifti/lh.xhemisphere.reg.surf.gii`
            # resample atlas into RHemi
            resampXhemID=`fsl_sub -q long.q -j $giftiXhemID wb_command -label-resample /vols/Data/soma/Atlases/Joern/${ROI_RH}.label.gii /vols/Data/soma/Atlases/Joern/rh.SPHERE.REG.surf.gii $surfDir/${subj}/gifti/lh.xhemisphere.reg.surf.gii ADAP_BARY_AREA $surfDir/$subj/gifti/ROI/${subj}.${ROI_RH}.R.label.gii -area-surfs /vols/Data/soma/Atlases/Joern/rh.midthickness.surf.gii $surfDir/${subj}/gifti/lh.xhemimidthickness.surf.gii`
            # project surf R.ROI to volume
            fsl_sub -q short.q -j $resampXhemID /vols/Data/soma/Adapticity/scripts/Face_scripts/fsSurfProjBackL.sh $subj $surfDir/$subj/gifti 1 $surfDir/$subj/gifti/ROI/${subj}.${ROI_RH}.R.label.gii ${ROI_RH}
        else
            # check if atlas has been resampled into RHemi
            if [ ! -e $SUBJECTS_DIR/${subj}/gifti/ROI/${subj}.${ROI_RH}.R.label.gii ]; then
                # resample atlas into RHemi
                resampXhemID=`fsl_sub -q long.q wb_command -label-resample /vols/Data/soma/Atlases/Joern/${ROI_RH}.label.gii /vols/Data/soma/Atlases/Joern/rh.SPHERE.REG.surf.gii $surfDir/${subj}/gifti/lh.xhemisphere.reg.surf.gii ADAP_BARY_AREA $surfDir/$subj/gifti/ROI/${subj}.${ROI_RH}.R.label.gii -area-surfs /vols/Data/soma/Atlases/Joern/rh.midthickness.surf.gii $surfDir/${subj}/gifti/lh.xhemimidthickness.surf.gii`
                # project surf R.ROI to volume
                fsl_sub -q short.q -j $resampXhemID /vols/Data/soma/Adapticity/scripts/Face_scripts/fsSurfProjBackL.sh $subj $surfDir/$subj/gifti 1 $surfDir/$subj/gifti/ROI/${subj}.${ROI_RH}.R.label.gii ${ROI_RH}
            #if [ ! -e $SUBJECTS_DIR/${subj}_adapt/gifti/ROI/${subj}.${ROI_RH}.R.label.gii ]; then
            #    # resample atlas into RHemi
            #    resampXhemID=`fsl_sub -q long.q wb_command -label-resample /vols/Data/soma/Atlases/Joern/${ROI_RH}.label.gii /vols/Data/soma/Atlases/Joern/rh.SPHERE.REG.surf.gii $surfDir/${subj}_adapt/gifti/lh.xhemisphere.reg.surf.gii ADAP_BARY_AREA $surfDir/${subj}_adapt/gifti/ROI/${subj}.${ROI_RH}.R.label.gii -area-surfs /vols/Data/soma/Atlases/Joern/rh.midthickness.surf.gii $surfDir/${subj}_adapt/gifti/lh.xhemimidthickness.surf.gii`
            #    # project surf R.ROI to volume
            #    fsl_sub -q short.q -j $resampXhemID /vols/Data/soma/Adapticity/scripts/Face_scripts/fsSurfProjBackL.sh $subj $surfDir/${subj}_adapt/gifti 1 $surfDir/${subj}_adapt/gifti/ROI/${subj}.${ROI_RH}.R.label.gii ${ROI_RH}
            else
                # check if R.ROI projected to Volume
                if [ ! -e $SUBJECTS_DIR/${subj}/gifti/Volume/${subj}_${ROI_RH}.ROI_rh_ribbon.nii.gz ]; then
                #if [ ! -e $SUBJECTS_DIR/${subj}_adapt/gifti/Volume/${subj}_${ROI_RH}.ROI_rh_ribbon.nii.gz ]; then
                    # project surf R.ROI to volume
                    fsl_sub -q short.q /vols/Data/soma/Adapticity/scripts/Face_scripts/fsSurfProjBackL.sh $subj $surfDir/$subj/gifti 1 $surfDir/$subj/gifti/ROI/${subj}.${ROI_RH}.R.label.gii ${ROI_RH}
                fi
            fi
        fi
    fi
fi
