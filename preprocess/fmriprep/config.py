import os
import pandas as pd 
'''
you can define yourself config in this file.
such as fmriprep cmd and bids dataset path.etc
'''


class fMRI_Prep_Job:
    # input data path
    bids_data_path  = "/data/liugroup/home/pdchen/ADNI/ADNI2_BIDS/"
    # 一个容器中处理多少个被试 
    step = 12
    # fmriprep opm thread
    thread = 9
    # max work contianers
    max_work_nums = 15

    # 在bids同级目录下创建processed文件夹
    bids_output_path = os.path.join("/".join(bids_data_path.split('/')[:-1]),'processed')
    if not os.path.exists(bids_output_path):
        os.mkdir(bids_output_path)
    # fmri work path 
    fmri_work="/data/liugroup/home/pdchen/ADNI/fmri_work"
    
    # freesurfer_license
    freesurfer_license = "/data/liugroup/home/pdchen/license.txt"
    # contianer id 
    contianer_id = "nipreps/fmriprep:20.2.5 "
    # fmriprep cmd 
    cmd ="docker run -it --rm -v {bids_data_path}:/data -v {freesurfer_license}:/opt/freesurfer/license.txt -v {bids_output_path}:/out -v {fmri_work}:/work {contianer_id} /data /out --skip_bids_validation   -w /work --omp-nthreads {thread} --fs-no-reconall --resource-monitor participant --participant-label {subject_ids} --output-spaces MNI152Lin:res-1:res-2"

class Result:
    path = "./result/"
    os.makedirs(path,exist_ok=True)


class PostProcess:
    """
    fmriprep 后处理数据
    """
    # 类型的名字
    task_type = "rest"
    # tasks 
    tasks = []
    
    dataset_path = os.path.join(fMRI_Prep_Job.bids_output_path,'fmriprep')

    store_path = os.path.join(fMRI_Prep_Job.bids_output_path,'post-process')

    t_r = 2.5

    low_pass = 0.08

    high_pass = 0.01

    n_process = 40

    if t_r != None:
        store_path = os.path.join(store_path,'filter','clean_imgs')
    else:
        store_path = os.path.join(store_path,'unfilter','clean_imgs')

    os.makedirs(store_path,exist_ok=True)

class RoiTs:
    """
    ROI 级别时间序列
    处理271个全脑roi
    """
    n_process = 40

    t_r = None
    
    low_pass = None

    high_pass = None
    flag_gs = False

    if flag_gs:
        file_name = "*with_gs.nii.gz"
        ts_file = "GS"
    else:
        file_name = "*without_gs.nii.gz"
        ts_file = "NO_GS"

    reg_path = os.path.join(PostProcess.store_path,"*",PostProcess.task_type,file_name)
    
    # reg_path = "/share/data2/dataset/ds002748/fmriprep/proprecced/*/rest/*without_gs.nii.gz"

    smoothing_fwhm = 6


    save_path = os.path.join("/".join(PostProcess.store_path.split('/')[:-1]),'timeseries',ts_file)

    os.makedirs(save_path,exist_ok=True)

class QC:
    '''
    质量控制
    这里留一个坑，以后再填
    '''