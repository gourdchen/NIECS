#!/bin/bash
3dmerge -1blur_fwhm 4.0 -doall -prefix r${run}_blur.nii \
          sub-08_task-flanker_run-${run}_space-MNI152NLin2009cAsym_res-2_desc-preproc_bold.nii.gz
