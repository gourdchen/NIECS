import nibabel as nib
import pandas as pd
import glob
import numpy as np
import os
def checkCenter(affine,dataShape):
    P = True
    for i in range(3):
        if(np.abs(affine[i,i]*dataShape[i]+2*affine[i,3])>50):
            P = False
    if(P == False):
        newAffine =affine.copy()
        for i in range(3):
            newAffine[i,3] = -affine[i,i] * 0.5 * (dataShape[i]+1)
    else:
        newAffine = affine

    return newAffine,P

def checkData(pathes):
    
    for i,path in enumerate(pathes):
        path = path.replace('\\','/')
        print(path.strip())

        img = nib.load(path)
        header = img.header
        affine = img.affine
        data = img.get_fdata()
        img.uncache()

        del img
        dataShape = data.shape

        #首先检查中心点位置,通过affine矩阵检查

        newAffine,P = checkCenter(affine,dataShape)
        if(not P):
            nib.Nifti1Image(data,newAffine).to_filename(path)
            print(path)

def checkData2(pathes):
    
    for i,path in enumerate(pathes):
        print(path.strip())

        img = nib.load(path)
        header = img.header
        affine = img.affine
        data = np.asarray(img.dataobj)

        dataShape = data.shape

        #首先检查中心点位置,通过affine矩阵检查

        newAffine = checkCenter(affine,dataShape)
        newPath = 'D:/DATA/ADNI_T1_2/'+os.path.basename(path)
        nib.Nifti1Image(data,newAffine).to_filename(newPath)
        
        print(str(i),end='\r')
# offset = [-102.6875,-91.57665,-53.88352,1]
# qform = header.get_qform()
# qform[:,3] = [-102.6875,-91.57665,-53.88352,1]
# header.set_qform(qform)
if __name__ == '__main__':
    
    # pathTable = pd.read_csv(r"G:\ADNI_fMRI\Parameter/ADNI_PATH_LIST.csv")
    # pathTable['PATH'] = pathTable['PATH'].apply(lambda x: x.replace('\\','/'))
    # with open(r"G:\ADNI_fMRI\Parameter\43slices1357_TR3000.txt",'r') as f:
    #     pathes = f.readlines()
    #pathes = glob.glob('M:/ADNI_fMRI_MB/*/brant_4D.nii')
    pathes = glob.glob('J:/ET/ET_DTI_22baseline/*/dti.nii')
    #print(pathes)
    checkData(pathes)

    
    