#fsSurf2Surf.sh $subject $natDir $dataInput $hemi $targetSurf $dirFreesurfer $direction

subj=$1 #SF11
natDir=$2 #/vols/Data/soma/Atlases/Joern/
dataInput=$3 #/vols/Data/soma/Atlases/Joern/ROI.label.gii
xhem=$4 # 0 or 1
targetSurf=$5 #/vols/Data/soma/6Finger/surf/SF1/gifti

hem=(L R)
hemh=(lh rh)
heml=(CORTEX_LEFT CORTEX_RIGHT)

#create output and input names
nametemp=${dataInput%%.gii}; filetype=${nametemp##*.}
nametemp=${dataInput%%.$filetype.gii}; nametemp=${nametemp%%.${hem[$xhem]}*}; nametemp=${nametemp##*.}; name=${nametemp##*/}
mkdir $targetSurf/ROI
dataOutput=$targetSurf/ROI/${subj}.$name.${hem[$xhem]}.$filetype.gii #output name: input name plus added tag: currently treats the bit before .L/.R or .func/.label as the name

#native surface
current_giisphere=$natDir/${hemh[$xhem]}.sphere.reg.surf.gii
current_midthick=$natDir/${hemh[$xhem]}.midthickness.surf.gii

#target surface
new_sphere=$targetSurf/${hemh[$xhem]}.sphere.reg.surf.gii
new_midthick=$targetSurf/${hemh[$xhem]}.midthickness.surf.gii

    if [[ -f $current_giisphere && -f $new_sphere && -f $current_midthick && -f $new_midthick ]]; then #check whether all files are there
      if [[ $filetype == "func" ]]; then
        wb_command -metric-resample $dataInput $current_giisphere $new_sphere ADAP_BARY_AREA $dataOutput -area-surfs $current_midthick $new_midthick
        wb_command -set-structure $dataOutput ${heml[$xhem]}

      elif [[ $filetype == "label" ]] ; then

        wb_command -label-resample $dataInput $current_giisphere $new_sphere ADAP_BARY_AREA $dataOutput -area-surfs $current_midthick $new_midthick
        wb_command -set-structure $dataOutput ${heml[$xhem]}
      else
        echo filetype not recognised: supports only func.gii or label.gii
      fi


    else #if files don't exist, first create sphere files from Freesurfer

      dirFreesurfer=$6 #E.g.: /vols/Data/soma/6Finger/surf/SF1
        fswhite=$dirFreesurfer/surf/${hemh[$xhem]}.white
        fspial=$dirFreesurfer/surf/${hemh[$xhem]}.pial
        current_fssphere=$dirFreesurfer/surf/${hemh[$xhem]}.sphere.reg

        if [[ -f $fswhite && $fspial && $current_fssphere ]]; then

          direction=$7
          if [[ $direction == "source" ]]; then
            /home/fs0/daanw/Scripts/wb_shortcuts -freesurfer-resample-prep $fswhite $fspial $current_fssphere $new_sphere $current_midthick $new_midthick $current_giisphere
            echo created $current_giisphere
          elif [[ $direction == "target" ]]; then #define the reg file of the target dir
            /home/fs0/daanw/Scripts/wb_shortcuts -freesurfer-resample-prep $fswhite $fspial $current_fssphere $current_giisphere $new_midthick $current_midthick $new_sphere
            echo created $new_sphere
          else
            echo direction can only be source or target
            exit
          fi

          #native surface
          current_giisphere=$natDir/${hemh[$xhem]}.sphere.reg.surf.gii
          current_midthick=$natDir/${hemh[$xhem]}.midthickness.surf.gii #created by prep
          #other surface
          new_sphere=$targetSurf/${hemh[$xhem]}.sphere.reg.surf.gii
          new_midthick=$targetSurf/${hemh[$xhem]}.midthickness.surf.gii #create by prep

          #resample
          if [[ $filetype == "func" ]]; then
            wb_command -metric-resample $dataInput $current_giisphere $new_sphere ADAP_BARY_AREA $dataOutput -area-surfs $current_midthick $new_midthick
            wb_command -set-structure $dataOutput ${heml[$xhem]}
          elif [[ $filetype == "label" ]]; then
            wb_command -label-resample $dataInput $current_giisphere $new_sphere ADAP_BARY_AREA $dataOutput -area-surfs $current_midthick $new_midthick
            wb_command -set-structure $dataOutput ${heml[$xhem]}
          else
            echo filetype not recognised: supports only func.gii or label.gii
          fi

        else
          echo Cannot find files, please supply correct Freesurfer directory
        fi
    fi
