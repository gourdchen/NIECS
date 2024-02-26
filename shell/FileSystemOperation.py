# author : PindongChen
# date : 2020/8/13

# list the file of one directory
def listFiles(PATH,pattern='*.nii',saveTxt='./image.txt'):
'''

'''
    dirList = os.listdir(PATH)
    imageNum = 0
    with open(saveTxt,'w') as f:
        for dir in dirList:
            imagePaths = glob.glob(os.path.join(path,dir,'*','*',pattern))
            if len(imagePaths)>0:
                for i in range(len(imagePaths)):
                    imageNum += 1
                    print(imagePaths[i])
                    f.write(imagePaths[i]+'\n')
        print(imageNum)


# move the ADNI image data to new directory
# original arrange form is just like Subject-Modal-Time-ImageNumber-DicomImage
# new file organization form is just like Subject-Time-Image
# the risk of repeated time existing
def arrangeADNI(PATH,newPATH,saveTxt='./image.txt',imageName='brant_4D.nii'):

    subjects = sorted(os.listdir(rootPath))

    with open(saveTxt, 'w') as f:
        for i in range(len(subjects)):
            subjectPath = os.path.join(PATH, subjects[i])
            newSubjectPath = os.path.join(newPATH,subjects[i])
            if not os.path.exists(newSubjectPath):
                os.mkdir(newSubjectPath)

            modalPaths = os.listdir(subjectPath)

            for modalPath in modalPaths:
                timePaths = os.listdir(os.path.join(subjectPath,modalPath))

                for timePath in timePaths:
                    imagePath = os.path.join(subjectPath,modalPath,timePath,imageName)
                    if os.path.exists(imagePath):

                        newTimePath = os.path.join(newSubjectPath,timePath[0:4]+timePath[5:7]+timePath[8:10])
                        if not os.path.exists(newTimePath):
                           os.makedirs(newTimePath)
                        newImagePath = os.path.join(newTimePath,imageName)
                        shutil.copy(imagePath,newTimePath)
                        print('Original image:',imagePath)
                        print('New Image:',newImagePath)
                        print(os.path.dirname(imagePath))
                        f.write(newTimePath)
                        f.write('\n')
                    else:
                        pass
                        #print(os.path.dirname(imagePath))