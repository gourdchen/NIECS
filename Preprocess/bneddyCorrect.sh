#!/bin/bash
folder="/mnt/j/ET/ET_DTI_22baseline"
files=`ls $folder`
for file in $files
do 
	bneddy -i ${folder}/${file}/DTI/sub.nii.gz -o ${folder}/${file}/DTI/eddy -ref 0
	bnrotate_bvec -i ${folder}/${file}/DTI/bvecs -log ${folder}/${file}/DTI/eddy.txt -o ${folder}/${file}/DTI/rotated_bvecs
done


