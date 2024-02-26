'''
the cat12 is crash, but there are some sMRI that are not segmented, find them by using the contrast between orginal file list and surf file list.
'''
import sys
sys.path.append('E:/brain/nits/')
from fileOperation import find_ADNI_filename,Glob

if __name__ == '__main__':
    OriginFileList = Glob('D:/DATA/ADNI/ADNI_T1/*.nii')
    SurfFileList = Glob('D:/DATA/ADNI/ADNI_T1/surf/lh.thickness*')
    PTIDs = []
    pPTIDs = []

    for file in sorted(OriginFileList):
        PTID = find_ADNI_filename(file)[0]
        PTIDs.append(PTID)
    for file in SurfFileList:
        PTID = find_ADNI_filename(file)[0]
        pPTIDs.append(PTID)

    for p in PTIDs:
        if(p not in pPTIDs):
            print(p)
    
