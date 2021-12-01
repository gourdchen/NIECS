import os
from nilearn import image as nimg
from nilearn import plotting as nplot
import numpy as np
import nibabel as nib
import pandas as pd
import glob

images = glob.glob('./out/fmriprep/*/ses-1/func/*MNI152Lin_res-2_*_bold.nii.gz')
for image in images:
    print(image)
    dirname = os.path.dirname(image)
    confound = glob.glob(os.path.join(dirname,'*confounds*.tsv'))[0]
    print(confound)
    mask = glob.glob(os.path.join(dirname,"*MNI152Lin_res-2_*_mask.nii.gz"))[0]
    print(mask)
    confound_df = pd.read_csv(confound,delimiter='\t')
    
    confound_vars = ['trans_x','trans_y','trans_z','rot_x','rot_y','rot_z','global_signal','a_comp_cor_01','a_comp_cor_02']
    confound_df = confound_df[confound_vars]
    for col in confound_df.columns:
        new_name = '{}_dt'.format(col)
        new_col = confound_df[col].diff()
        confound_df[new_name] = new_col
        confound_df.head()
    raw_func_img = nimg.load_img(image)
    func_img = raw_func_img.slicer[:,:,:,10:]
    drop_confound_df = confound_df.loc[10:]
    confounds_matrix = drop_confound_df.values

    high_pass= 0.009
    low_pass = 0.08
    t_r = 2
    clean_img = nimg.clean_img(func_img,confounds=confounds_matrix,detrend=True,standardize=True,
                            low_pass=low_pass,high_pass=high_pass,t_r=t_r, mask_img=mask)
    smooth_img = nimg.smooth_img(clean_img,[6,6,6])
    smooth_img.to_filename(os.path.join(dirname,'smooth6.nii.gz'))
                            



