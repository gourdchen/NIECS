import os
import nibabel as nib
import nilearn
from nilearn import image
import numpy as np
import glob
import shutil
import pandas as pd
import json
import re
def conver3Dto4D(partterns,saveName):
    concatImage = image.concat_imgs(partterns)
    concatImage.to_filename(saveName)
def convertS02():
    baseDir = r"J:\AD\MCAD\REST\AD_S02\AD_S02_RS"
    for dirname in os.listdir(baseDir):
        print(dirname)
        saveName = os.path.join(baseDir,dirname,'brant_4D.nii.gz')
        conver3Dto4D(os.path.join(baseDir,dirname,'Rest_*.nii'), saveName)

def constructSliceTiming(sliceNumber,TR):
    if(sliceNumber%2==0):
        sliceOrder = [i for i in range(1,sliceNumber,2)]
        sliceOrder.extend([i for i in range(0,sliceNumber-1,2)])
    else:
        sliceOrder = [i for i in range(0,sliceNumber,2)]
        sliceOrder.extend([i for i in range(1,sliceNumber-1,2)])
    sliceOrder = np.asarray(sliceOrder).astype(np.int16)
    timeSequence = np.linspace(0, 2,num=sliceNumber,endpoint=False)
    sliceTiming = np.zeros(sliceNumber)
    sliceTiming[sliceOrder] = timeSequence
    sliceTiming = sliceTiming.tolist()
    return sliceTiming

def nameParttern():
    ['brat_4D.nii','brant_4D.nii.gz','brant_S021.nii','brant_4D.nii','brant_4D.nii','f+dirname','brant_4D.nii']
def moveAndRename():
    baseDir = "J:/AD/BIDS"
    nameMapping = pd.DataFrame(columns=['center','subj','nsubj','flag','sMRI','fMRI'])
    if(not os.path.exists(baseDir)):
        os.mkdir(baseDir)
    subP = 1
    for center in range(1,8):
        centerfMRIDir = "J:/AD/MCAD/REST/AD_S0%d/AD_S0%d_RS" % (center,center)
        centersMRIDir = "J:/AD/MCAD/sMRI/AD_S0%d/AD_S0%d_MPR" % (center,center)
        print('center:',center)
        for dirname in os.listdir(centerfMRIDir):
            nsubj = "sub-{:0>4}".format(subP)
            subP +=1
            if(not os.path.isdir(os.path.join(centerfMRIDir,dirname))):
                continue
            print(dirname,nsubj)
            if(center!=6):
                fMRI = glob.glob(os.path.join(centerfMRIDir,dirname,'bra*.nii*'))
            else:
                fMRI = glob.glob(os.path.join(centerfMRIDir,dirname,'f'+dirname[2:]+'*.nii*'))
            sMRI = os.path.join(centersMRIDir,dirname+'.nii')
            if(not os.path.exists(sMRI)):
                name1 = re.findall('\d*_*\d_[NMA][CD]', os.path.basename(sMRI))
                if(len(name1)==0):
                    continue
                name1 = name1[0]
                name2 = re.findall('\d{3}_*\d*', os.path.basename(sMRI))[0]
                name = name1+name2
                sMRIs = glob.glob(os.path.join(centersMRIDir,"*"+name+'.nii'))
                if(len(sMRIs)>0):
                    sMRI = sMRIs[0]
                    print('Not find its sMRI, but find another visit sMRI',sMRI)
                else:
                    name3 = re.findall('\d{3}', name2)[0]
                    name = name1+name3
                    sMRIs = glob.glob(os.path.join(centersMRIDir,name+'*.nii'))
                    if(len(sMRIs)>0):
                        sMRI = sMRIs[0]
                        print('Not find its sMRI, but find another visit sMRI',sMRI)
                    else:
                        print(dirname,'sMRI error, please check')
                        nameMapping = nameMapping.append(pd.DataFrame({'center':center,'subj':dirname,'nsubj':nsubj,'flag':0,'fMRI':fMRI,'sMRI':sMRI},index=[0]))
                        #nameMapping.to_csv('J:/AD/BIDS/info.csv')
                        continue
            if((len(fMRI)<1) or (len(fMRI)>1) ):
                print(dirname,'have error ,please check!')
                nameMapping = nameMapping.append(pd.DataFrame({'center':center,'subj':dirname,'nsubj':nsubj,'flag':0,'fMRI':fMRI,'sMRI':sMRI},index=[0]))
                continue

            fMRI = fMRI[0]
            if(not os.path.exists(os.path.join(baseDir,nsubj))):
                os.mkdir(os.path.join(baseDir,nsubj))
            if(not os.path.exists(os.path.join(baseDir,nsubj,'ses-1'))):
                os.mkdir(os.path.join(baseDir,nsubj,'ses-1'))
                if(not os.path.exists(os.path.join(baseDir,nsubj,'ses-1','func'))):
                    os.mkdir(os.path.join(baseDir,nsubj,'ses-1','func'))
                    
                if(not os.path.exists(os.path.join(baseDir,nsubj,'ses-1','anat'))):
                    os.mkdir(os.path.join(baseDir,nsubj,'ses-1','anat'))
                destin = os.path.join(baseDir,nsubj,'ses-1')
                excMove(fMRI, sMRI, nsubj,destin)
                
                nameMapping = nameMapping.append(pd.DataFrame({'center':center,'subj':dirname,'nsubj':nsubj,'flag':1,'fMRI':fMRI,'sMRI':sMRI},index=[0]))
                
                nameMapping.to_csv('J:/AD/BIDS/info.csv')
                #break  
def excMove(fMRI,sMRI,nsubj,dirname):
    shape = nib.load(fMRI).header.get_data_shape()
    sliceNumber = shape[2]
    sliceTiming = constructSliceTiming(sliceNumber, 2)
    infoJson = {}
    infoJson["RepetitionTime"]=2
    infoJson["TaskName"]='rest'
    infoJson["SliceTiming"]=sliceTiming
    shutil.copy(fMRI, os.path.join(dirname,'func',nsubj+'_ses-1_task-rest_run-0_bold.'+fMRI.split('.')[-1]))
    with open(os.path.join(dirname,'func',nsubj+'_ses-1_task-rest_run-0_bold.json'),'w') as f:
        json.dump(infoJson, f)
    shutil.copy(sMRI, os.path.join(dirname,'anat',nsubj+'_ses-1_run-0_T1w.'+fMRI.split('.')[-1]))


if __name__ == "__main__":
    moveAndRename()