import nibabel as nib
import numpy as np
from nilearn import surface
import os
import matplotlib as mpl
import time
import matplotlib.pyplot as plt
from nilearn import datasets
from nilearn import plotting
fsaverage = datasets.fetch_surf_fsaverage()
import seaborn as sns
def mappingParcellToVolume(data,atlas):
    if(isinstance(atlas,str)):
        atlas = nib.load(atlas)
    atlas_data = atlas.get_fdata()
    atlas.uncache()
    new_data = np.zeros_like(atlas_data)
    atlas_data = np.nan_to_num(atlas_data)
    rois = np.unique(atlas_data[:])[1:]
    for i,roi in enumerate(rois):
        new_data[atlas_data==roi] = data[i]
    newImage = nib.Nifti1Image(new_data,atlas.affine)
    return newImage
def volumeToSurface(image,interpolation='linear'):
    fsaverageL = r"E:\brain\BNatlas\BN_Atlas_freesurfer\fsaverage\fsaverage_LR32k\fsaverage.L.inflated.32k_fs_LR.surf.gii"
    fsaverageR = r"E:\brain\BNatlas\BN_Atlas_freesurfer\fsaverage\fsaverage_LR32k\fsaverage.R.inflated.32k_fs_LR.surf.gii"
    textureL = surface.vol_to_surf(image,fsaverageL,inner_mesh=r"E:\brain\BNatlas\BN_Atlas_freesurfer\fsaverage\fsaverage_LR32k\fsaverage.L.white.32k_fs_LR.surf.gii")
    textureR = surface.vol_to_surf(image,fsaverageR,inner_mesh=r"E:\brain\BNatlas\BN_Atlas_freesurfer\fsaverage\fsaverage_LR32k\fsaverage.R.white.32k_fs_LR.surf.gii")
    
    #textureL = surface.vol_to_surf(image,fsaverageL,radius=4,interpolation=interpolation,kind='line',mask_img='Mask.nii')
    #textureR = surface.vol_to_surf(image,fsaverageR,radius=4,interpolation=interpolation,kind='line',mask_img='Mask.nii')
    
    newL = nib.GiftiImage(header=nib.load(r"E:\brain\GS\surface\NC_tmap.nii.L.func.gii").header)
    newR = nib.GiftiImage(header=nib.load(r"E:\brain\GS\surface\NC_tmap.nii.R.func.gii").header)

    dataArrayL = nib.gifti.gifti.GiftiDataArray(textureL.astype(np.float32))
    dataArrayR = nib.gifti.gifti.GiftiDataArray(textureR.astype(np.float32))

    newL.add_gifti_data_array(dataArrayL)
    newR.add_gifti_data_array(dataArrayR)

    return newL,newR

def GMV_Mapping(PATH,pos_max=None,pos_min=None,neg_max=None,neg_min=None,pcmap=None,ncmap=None,MAX=False):
    from matplotlib import cm
    cmd = 'E:/matTool/workbench/bin_windows64/wb_command.exe -volume-to-surface-mapping  %s \
            E:/brain/BNatlas/BN_Atlas_freesurfer/fsaverage/fsaverage_LR32k/fsaverage.L.inflated.32k_fs_LR.surf.gii %s -trilinear'
    cmd2 = 'E:/matTool/workbench/bin_windows64/wb_command.exe -volume-to-surface-mapping  %s \
            E:/brain/BNatlas/BN_Atlas_freesurfer/fsaverage/fsaverage_LR32k/fsaverage.R.inflated.32k_fs_LR.surf.gii %s -trilinear'
    
    
    for path in PATH:
        dir = os.path.dirname(path)
        name = os.path.basename(path)
        
        CMD = cmd % (path,'%s/' % dir+name+'.L.func.gii')
        print(CMD)
        print(os.system(CMD))
        CMD = cmd2 % (path,'%s/' % dir+name+'.R.func.gii')
        print(os.system(CMD))
    time.sleep(5)
    for path in PATH:
        dir = os.path.dirname(path)
        name = os.path.basename(path)
        L_data = nib.load('%s/' % dir+name+'.L.func.gii').agg_data()*100
        R_data = nib.load('%s/' % dir+name+'.R.func.gii').agg_data()*100

        Data = np.concatenate([L_data, R_data])
        if(MAX):
            if(np.sum(Data>0) > 0):
                print('Postive:',)
                print('min:',np.min(Data[Data>0]),'max:',np.max(Data[Data>0]))
            if(np.sum(Data<0) > 0):
                print('Negative:',)
                print('min:',np.min(Data[Data<0]),'max:',np.max(Data[Data<0]))
        Data[np.abs(Data)<1] = 0
        if(pos_max is None):
            pos_max = np.max(Data[Data>0])
        if(pos_min is None):
            pos_min = np.min(Data[Data>0])
        if(neg_max is None):
            neg_max = np.max(Data[Data<0])
        if(neg_min is None):
            neg_min = np.min(Data[Data<0])
        norm_p = mpl.colors.Normalize(vmin=pos_min, vmax=pos_max)
        norm_n = mpl.colors.Normalize(vmin=neg_min, vmax=neg_max)

        colorMapping_p = cm.ScalarMappable(norm=norm_p, cmap = pcmap)
        colorMapping_n = cm.ScalarMappable(norm=norm_n, cmap = ncmap)

        labelDict = {}
        for i, p in enumerate(Data):
            colorValue = (1,1,1,1)
            if(p>0):
                colorValue = colorMapping_p.to_rgba(p)
            elif(p<0):
                colorValue = colorMapping_n.to_rgba(p)
            labelDict[p] = (i, colorValue)

        names = ['CIFTI_STRUCTURE_CORTEX_LEFT' for i in range(L_data.shape[0])]
        names.extend(['CIFTI_STRUCTURE_CORTEX_RIGHT' for i in range(R_data.shape[0])])
        verteces = [i for i in range(L_data.shape[0])]
        verteces.extend([i for i in range(L_data.shape[0])])
        verteces = np.asarray(verteces)
        brainModelAxis = nib.cifti2.cifti2_axes.BrainModelAxis(name=names, vertex=np.asarray(verteces),
                                                               nvertices={'CIFTI_STRUCTURE_CORTEX_LEFT': 32492,
                                                                          'CIFTI_STRUCTURE_CORTEX_RIGHT': 32492}, )
        newLabelAxis = nib.cifti2.cifti2_axes.LabelAxis(['aaa'], labelDict)
        newheader = nib.cifti2.cifti2.Cifti2Header.from_axes((newLabelAxis, brainModelAxis))
        newImage = nib.cifti2.cifti2.Cifti2Image(dataobj=Data.reshape([1, -1]), header=newheader)
        newImage.to_filename('%s/' % dir+name+'.dlabel.nii')
        
def GMV_MappingAtlas(PATH, pos_max, pos_min, neg_max, neg_min, pcmap, ncmap, MAX=False,
                nii_path=r"E:\brain\BNatlas\BN_Atlas_274_with_cerebellum_without_255.nii",savePath = '',saveName=''):
    from nilearn import surface
    fsaverageL = r"E:\brain\BNatlas\BN_Atlas_freesurfer\fsaverage\fsaverage_LR32k\fsaverage.L.inflated.32k_fs_LR.surf.gii"
    fsaverageR = r"E:\brain\BNatlas\BN_Atlas_freesurfer\fsaverage\fsaverage_LR32k\fsaverage.R.inflated.32k_fs_LR.surf.gii"
    dlable = nib.load(
        r"E:\brain\BNatlas\BN_Atlas_freesurfer\fsaverage\fsaverage_LR32k\fsaverage.BN_Atlas.32k_fs_LR.dlabel.nii")
    llabel = nib.load(r"E:\brain\BNatlas\BN_Atlas_freesurfer\fsaverage\fsaverage_LR32k\fsaverage.L.BN_Atlas.32k_fs_LR.label.gii")
    rlabel = nib.load(r"E:\brain\BNatlas\BN_Atlas_freesurfer\fsaverage\fsaverage_LR32k\fsaverage.R.BN_Atlas.32k_fs_LR.label.gii")
    llable_data = llabel.agg_data()
    rlable_data = rlabel.agg_data()
    dlabel_data = np.asarray(dlable.dataobj)
    nii = nib.load(nii_path)
    template = np.nan_to_num(nii.get_fdata())
    rois = np.unique(template[:])[1:]
    BrianModelAxis = dlable.header.get_axis(1)

    for path in PATH:
        if(isinstance(path,str)):
            dir = os.path.dirname(path)
            name = os.path.basename(path)
            image = nib.load(path)
            imageData = image.get_fdata()
            image.uncache()
        else:
            image = path
            imageData = image.get_fdata()   
        #del image
        imageData = np.nan_to_num(imageData)
        if (MAX):
            if (np.sum(imageData > 0) > 0):
                print('Postive:', )
                print('min:', np.min(imageData[imageData > 0]), 'max:', np.max(imageData[imageData > 0]))
            if (np.sum(imageData < 0) > 0):
                print('Negative:', )
                print('min:', np.min(imageData[imageData < 0]), 'max:', np.max(imageData[imageData < 0]))

        norm_p = mpl.colors.Normalize(vmin=pos_min, vmax=pos_max)
        norm_n = mpl.colors.Normalize(vmin=neg_min, vmax=neg_max)
        colorMapping_p = mpl.cm.ScalarMappable(norm=norm_p, cmap=pcmap)
        colorMapping_n = mpl.cm.ScalarMappable(norm=norm_n, cmap=ncmap)
        labelDict = {}
        #for i in range(1,421):
        #    labelDict[i] = (labelDict[i][0],( 1, 1, 1, 1))
        for roi in range(1,211):
            fvalue = imageData[template == roi][0]
            if(fvalue == 0):
                colorValue = (1,1,1,1)
            elif(fvalue > 0):
                colorValue = colorMapping_p.to_rgba(fvalue)
            else:
                colorValue = colorMapping_n.to_rgba(fvalue)
            labelDict[roi] = (roi, colorValue)
            labelDict[roi+210] = (roi+210, colorValue)

        imageData[template<211] = 0
        NewImage = nib.Nifti1Image(imageData,image.affine)
        textureL = surface.vol_to_surf(NewImage, fsaverageL,
                                       inner_mesh=r"E:\brain\BNatlas\BN_Atlas_freesurfer\fsaverage\fsaverage_LR32k\fsaverage.L.white.32k_fs_LR.surf.gii")
        textureR = surface.vol_to_surf(NewImage, fsaverageR,
                                       inner_mesh=r"E:\brain\BNatlas\BN_Atlas_freesurfer\fsaverage\fsaverage_LR32k\fsaverage.R.white.32k_fs_LR.surf.gii")

        #Data[np.abs(Data) < 1] = 0

        textureL = textureL* 1000
        textureR = textureR* 1000
        textureL[np.abs(textureL) < 421] = 0
        textureR[np.abs(textureR) < 421] = 0
        Data = np.concatenate([textureL, textureR])


        norm_p = mpl.colors.Normalize(vmin=pos_min*1000, vmax=pos_max*1000)
        norm_n = mpl.colors.Normalize(vmin=neg_min*1000, vmax=neg_max*1000)
        colorMapping_p = mpl.cm.ScalarMappable(norm=norm_p, cmap=pcmap)
        colorMapping_n = mpl.cm.ScalarMappable(norm=norm_n, cmap=ncmap)
        for i, p in enumerate(Data):
            colorValue = (1, 1, 1, 1)
            if (p > 0):
                colorValue = colorMapping_p.to_rgba(p)
            elif (p < 0):
                colorValue = colorMapping_n.to_rgba(p)
            labelDict[p] = (p, colorValue)

        textureL[BrianModelAxis.vertex[:29696]] = dlabel_data[0,:29696]
        textureR[BrianModelAxis.vertex[29696:]] = dlabel_data[0,29696:]
        textureL[llable_data!=-1] = llable_data[llable_data!=-1]
        textureR[rlable_data!=-1] = rlable_data[rlable_data!=-1]
        Data = np.concatenate([textureL, textureR])

        names = ['CIFTI_STRUCTURE_CORTEX_LEFT' for i in range(textureL.shape[0])]
        names.extend(['CIFTI_STRUCTURE_CORTEX_RIGHT' for i in range(textureR.shape[0])])
        verteces = [i for i in range(textureL.shape[0])]
        verteces.extend([i for i in range(textureR.shape[0])])
        verteces = np.asarray(verteces)
        brainModelAxis = nib.cifti2.cifti2_axes.BrainModelAxis(name=names, vertex=np.asarray(verteces),
                                                               nvertices={'CIFTI_STRUCTURE_CORTEX_LEFT': 32492,
                                                                          'CIFTI_STRUCTURE_CORTEX_RIGHT': 32492}, )
        newLabelAxis = nib.cifti2.cifti2_axes.LabelAxis(['aaa'], labelDict)
        newheader = nib.cifti2.cifti2.Cifti2Header.from_axes((newLabelAxis, brainModelAxis))
        newImage = nib.cifti2.cifti2.Cifti2Image(dataobj=Data.reshape([1, -1]), header=newheader)
        newImage.to_filename(savePath+'/' +saveName+ '.dlabel.nii')


def ViewSurface(image,threshold=1.94):
    fsaverageL = r"E:\brain\atlas\fsaverage\pial_left.gii"
    fsaverageR = r"E:\brain\atlas\fsaverage\pial_right.gii"
    textureL = surface.vol_to_surf(image,fsaverage.pial_left,inner_mesh=fsaverage.white_left)
    textureR = surface.vol_to_surf(image,fsaverage.pial_right,inner_mesh=fsaverage.white_right)
    
    fig,axes = plt.subplots(1,2,figsize=[10,6],subplot_kw={'projection': '3d'})
    vmax = np.max([np.abs(textureL),np.abs(textureR)])
    
    plotting.plot_surf_stat_map(fsaverage.pial_left,textureL, hemi='left',
                            threshold=threshold,
                            bg_map=fsaverage.sulc_right,
                            cmap=sns.color_palette('cold_hot',as_cmap=True),
                            darkness=0.5,
                            colorbar=False,
                            #symmetric_cbar=True,
                            bg_on_data = True,
                            axes=axes[0],
                            vmax=vmax,
                            figure=fig
                           )
    
    plotting.plot_surf_stat_map(fsaverage.pial_right,textureR, hemi='right',
                        threshold=threshold,
                        bg_map=fsaverage.sulc_right,
                        cmap=sns.color_palette('cold_hot',as_cmap=True),
                        darkness=0.5,
                        colorbar=False,
                        #symmetric_cbar=True,
                       bg_on_data = True,
                        axes=axes[1],
                        vmax=vmax,
                            figure=fig
                       )
    plt.show()
    fig2,axes2 = plt.subplots(1,2,figsize=[10,6],subplot_kw={'projection': '3d'})
    plotting.plot_surf_stat_map(fsaverage.pial_left,textureL, hemi='right',
                        threshold=threshold,
                        bg_map=fsaverage.sulc_right,
                        cmap=sns.color_palette('cold_hot',as_cmap=True),
                        darkness=0.5,
                        colorbar=False,
                        #symmetric_cbar=True,
                       bg_on_data = True,
                        axes=axes2[0],
                        vmax=vmax,
                            figure=fig2
                       )
    plotting.plot_surf_stat_map(fsaverage.pial_right,textureR, hemi='left',
                        threshold=threshold,
                        bg_map=fsaverage.sulc_right,
                        cmap=sns.color_palette('cold_hot',as_cmap=True),
                        darkness=0.5,
                        colorbar=True,
                        #symmetric_cbar=True,
                       bg_on_data = True,
                        axes=axes2[1],
                        vmax=vmax,
                            figure=fig2
                       )
    plt.show()