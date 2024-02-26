#!/bin/bash
ses='ses-6'

for subj in `ls BIDS`
do
    echo ${subj:4}
    if [ ! -d "BIDS/${subj}/${ses}" ];then
		mkdir BIDS/${subj}/${ses}
        fi


            file=`ls fMRI/6month6H_ET_preprocess/${subj:4}*/*.nii`
            if test -z "$file"; then
                echo "The result is empty."
            else
            if [ ! -d "BIDS/${subj}/${ses}/func" ];then
			mkdir BIDS/${subj}/${ses}/func
            fi
            mv $file BIDS/${subj}/${ses}/func/${subj}_${ses}_task-rest_run-0_bold.nii
            cp /mnt/j/ET/BIDS/sub-429304/ses-1/func/sub-429304_ses-1_task-rest_run-0_bold.json BIDS/${subj}/${ses}/func/${subj}_${ses}_task-rest_run-0_bold.json
            fi
            
      
        if [ ! -d "BIDS/${subj}/${ses}/anat" ];then
			mkdir BIDS/${subj}/${ses}/anat
        fi
			file=`ls data_beforeresample/post_month6_${subj:4}*/t1.nii.gz`
            
			cp $file BIDS/${subj}/${ses}/anat/${subj}_${ses}_run-0_T1w.nii.gz
done