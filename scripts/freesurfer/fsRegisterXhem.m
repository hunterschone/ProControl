function S=fsRegisterXhem(subj)
%
% v1.0 Joern Diedrichsen (j.diedrichsen@ucl.ac.uk)
%
subject_dir='/misc/data19/schonehr/ProControl/data/DONE/sub-co01/surfaces';

old_dir=getenv('SUBJECTS_DIR');
setenv('SUBJECTS_DIR',subject_dir);

target=1;         % Target direction
hemisphere=[1:2]; % Do both hemispheres

for s=1:length(subj)
    
    subj_dir=[subject_dir filesep subj filesep];
    
    if (any(hemisphere==1))
        system(['/opt/freesurfer-600/bin/surfreg --s ' subj ' --t fsaverage_sym --lh']);
    end;
    
    if (any(hemisphere==2))
        system(['/opt/freesurfer-600/bin/xhemireg --s ' subj]);
        system(['/opt/freesurfer-600/bin/surfreg --s ' subj ' --t fsaverage_sym --lh --xhemi']);
    end;   
end;
end

