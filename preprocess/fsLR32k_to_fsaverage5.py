import os
wb_command = '~/software/workbench/bin_linux64/wb_command'

import glob
import os

image_names = glob.glob("/user/home/pdchen/MCAD/processed_fs/post-process/clean_imgs/sub-*/GSR_clean_filer.dtseries.nii.gz")

current_L_sphere = "standard_mesh_atlases/resample_fsaverage/fs_LR-deformed_to-fsaverage.L.sphere.32k_fs_LR.surf.gii"
current_R_sphere = "standard_mesh_atlases/resample_fsaverage/fs_LR-deformed_to-fsaverage.R.sphere.32k_fs_LR.surf.gii"

fs5_L_sphere = "standard_mesh_atlases/resample_fsaverage/fsaverage5_std_sphere.L.10k_fsavg_L.surf.gii"
fs5_R_sphere = "standard_mesh_atlases/resample_fsaverage/fsaverage5_std_sphere.R.10k_fsavg_R.surf.gii"

current_L_va = "standard_mesh_atlases/resample_fsaverage/fs_LR.L.midthickness_va_avg.32k_fs_LR.shape.gii"
current_R_va = "standard_mesh_atlases/resample_fsaverage/fs_LR.R.midthickness_va_avg.32k_fs_LR.shape.gii"

fs5_L_va = "standard_mesh_atlases/resample_fsaverage/fsaverage5.L.midthickness_va_avg.10k_fsavg_L.shape.gii"
fs5_R_va = "standard_mesh_atlases/resample_fsaverage/fsaverage5.R.midthickness_va_avg.10k_fsavg_R.shape.gii"


separate_command = '{wb_command} -cifti-separate {dtseries} COLUMN -metric CORTEX_LEFT {cortex_left} -metric CORTEX_RIGHT {cortex_right}'
resample_command_L = '{wb_command} -metric-resample {cortex_left} {current_L_sphere} {fs5_L_sphere} ADAP_BARY_AREA {fs5_func_L} -area-metrics {current_L_va} {fs5_L_va}'
resample_command_R = '{wb_command} -metric-resample {cortex_right} {current_R_sphere} {fs5_R_sphere} ADAP_BARY_AREA {fs5_func_R} -area-metrics {current_R_va} {fs5_R_va}'

for image_name in image_names:
    dir_name = os.path.dirname(image_name)
    cortex_left = 'temp_left.func.gii'
    cortex_right = 'temp_right.func.gii'
    fs5_func_L = os.path.join(dir_name,'GSR_clean_filter_fs5.L.func.gii')
    fs5_func_R = os.path.join(dir_name,'GSR_clean_filter_fs5.R.func.gii')

    print(os.system(separate_command.format(wb_command=wb_command,dtseries=image_name,cortex_left=cortex_left,cortex_right=cortex_right)))
    print(os.system(resample_command_L.format(wb_command=wb_command,cortex_left=cortex_left,
                    current_L_sphere=current_L_sphere,fs5_L_sphere=fs5_L_sphere,fs5_func_L=fs5_func_L,current_L_va=current_L_va,fs5_L_va=fs5_L_va)))
    print(os.system(resample_command_R.format(wb_command=wb_command,cortex_right=cortex_right,
                    current_R_sphere=current_R_sphere,fs5_R_sphere=fs5_R_sphere,fs5_func_R=fs5_func_R,current_R_va=current_R_va,fs5_R_va=fs5_R_va)))

    print(image_name)
