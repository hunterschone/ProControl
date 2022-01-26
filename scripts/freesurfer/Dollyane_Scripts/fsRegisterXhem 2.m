function S=fsRegisterXhem(subj)
%
% v1.0 Joern Diedrichsen (j.diedrichsen@ucl.ac.uk)
%
subject_dir='/vols/Data/soma/pre-post/surfaces/sub-aa03/';

old_dir=getenv('SUBJECTS_DIR');
setenv('SUBJECTS_DIR',subject_dir);
               
target=1;         % Target direction
hemisphere=[1:2]; % Do both hemispheres

for s=1:length(subj)
    
    subj_dir=[subject_dir filesep subj{s} filesep];
    
    if (any(hemisphere==1))
        system(['surfreg --s ' subj{s} ' --t fsaverage_sym --lh']);
    end;
    
    if (any(hemisphere==2))
        system(['xhemireg --s ' subj{s}]);
        system(['surfreg --s ' subj{s} ' --t fsaverage_sym --lh --xhemi']);
    end;   
end;
end

