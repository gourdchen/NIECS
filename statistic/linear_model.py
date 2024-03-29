import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import ttest_ind,ttest_1samp,ttest_rel
from statsmodels.stats.multitest import fdrcorrection
from nilearn.glm.second_level import SecondLevelModel
from nilearn.glm import threshold_stats_img
from view import volumeToSurface
import numpy as np
from nilearn import plotting
import matplotlib.pyplot as plt
import nibabel as nib

def to_categorical(y, num_classes=None):
    """Converts a class vector (integers) to binary class matrix.

    E.g. for use with categorical_crossentropy.
    # Arguments
        y: class vector to be converted into a matrix
            (integers from 0 to num_classes).
        num_classes: total number of classes.
    # Returns
        A binary matrix representation of the input.
    """
    y = np.array(y, dtype='int')
    input_shape = y.shape
    if input_shape and input_shape[-1] == 1 and len(input_shape) > 1:
        input_shape = tuple(input_shape[:-1])
    y = y.ravel()
    if not num_classes:
        num_classes = np.max(y) + 1
    n = y.shape[0]
    categorical = np.zeros((n, num_classes))
    categorical[np.arange(n), y] = 1
    output_shape = input_shape + (num_classes,)
    categorical = np.reshape(categorical, output_shape)
    return categorical
def regression(data,feature,covariance):
    formula = feature + '~ 1+' + covariance
    res = smf.ols(formula,data=data).fit()
    return res.resid

def oneway_Anova(data,feature,way):
    a = feature + '~' + way
    print(a)
    res = smf.ols(a,data=data).fit()
    res = anova_lm(res)
    return res

def regress_cov(features, covariance, center=True, keep_scale=True):
    """
    :param covarance: covariance
    :param center: Boolean, wether to add intercept
    """
    if features.ndim == 1:
        features = features.reshape(len(features), 1)
    if covariance.ndim == 1:
        covariance = covariance.reshape(len(features), 1)
    residuals = np.zeros_like(features)
    result = np.zeros_like(features)
    if center is True:
        b = covariance
    else:
        b = np.hstack([covariance, np.ones([covariance.shape[0], 1])])
    for f in range(features.shape[1]):
        w = np.linalg.lstsq(b, features[:, f])[0]
        if center is True:
            residuals[:, f] = features[:, f] - covariance.dot(w)
        else:
            residuals[:, f] = features[:, f] - covariance.dot(w[:-1])
    if keep_scale is True:
        for f in range(features.shape[1]):
            if np.min(features[:, f]) == np.max(features[:, f]):
                result[:, f] = features[:, f]
            else:
                result[:, f] = MinMaxScaler(feature_range=(np.min(features[:, f]), np.max(features[:, f]))). \
                    fit_transform(residuals[:, f].reshape(-1, 1)).flatten()
    else:
        result = residuals
    return result

def voxel_t_test(Data_1, Data_2, maskImage, cov=None):
    maskData = maskImage.get_fdata()
    
    tRes = np.zeros_like(maskData[maskData > 0])
    pRes = []
    if(cov is not None):
        if(Data_2 is not None):
            data = np.concatenate([Data_1,Data_2])
            print(data.shape)
            data_r = regress_cov(data, cov,center=False,keep_scale=True)
            Data_1 = data_r[:Data_1.shape[0],:]
            Data_2 = data_r[Data_1.shape[0]:,:]
        else:
            Data_1 = regress_cov(Data_1, cov,center=False,keep_scale=True)

    if(Data_2 is not None):
        print('1')
        tRes, pRes = ttest_ind(Data_1, Data_2)
        #print(tRes)

    else:
        for i in range(maskData[maskData > 0].shape[0]):
            t, p = ttest_1samp(Data_1[:,i],0)
            tRes[i] = t
            pRes.append(p)

    pRes = np.asarray(pRes)
    _, fdrP = fdrcorrection(pRes)
    tData = np.zeros_like(maskData)
    tData[maskData > 0] = tRes
    tImage = nib.Nifti1Image(tData, maskImage.affine)

    tData = np.zeros_like(maskData)
    ctRes = tRes.copy()
    ctRes[fdrP > 0.05] = 0
    tData[(maskData > 0)] = ctRes
    tImageC = nib.Nifti1Image(tData, maskImage.affine)

    return tImage, tImageC
def t_test(Data_1, Data_2, cov=None):
 
    tRes = np.zeros(Data_1.shape[1])
    pRes = []
    if(cov is not None):
        if(Data_2 is not None):
            Data = regress_cov(np.concatenate([Data_1,Data_2],axis=0), cov,center=False,keep_scale=True)
            Data_1 = Data[:Data_1.shape[0],:]
            Data_2 = Data[Data_1.shape[0]:,:]

    if(Data_2 is not None):
        for i in range(Data_1.shape[1]):
            t, p = ttest_ind(Data_1[:,i], Data_2[:,i])
            tRes[i] = t
            pRes.append(p)
    else:
        for i in range(Data_1.shape[1]):
            t, p = ttest_1samp(Data_1[:,i],0)
            tRes[i] = t
            pRes.append(p)

    pRes = np.asarray(pRes)
    _, fdrP = fdrcorrection(pRes)
    return tRes,  pRes, fdrP

def GLM(GLM_Input,design_matrix,contrast,filename,mask):
    
    second_level_model = SecondLevelModel(mask_img=mask)
    second_level_model = second_level_model.fit(GLM_Input,
                                                design_matrix=design_matrix,
                                                )
    z_map = second_level_model.compute_contrast(second_level_contrast=contrast,
                                                output_type='z_score')
    from nilearn.glm import threshold_stats_img
    thresholded_map2, threshold2 = threshold_stats_img(
        z_map, alpha=.05, height_control='fdr', mask_img=mask)
    print('The FDR=.05 threshold is %.3g' % threshold2)
    plotting.plot_stat_map(thresholded_map2,
                           title='z map, expected .05',
                           # threshold=threshold2,
                           draw_cross=False,
                           cut_coords=[28, 0, 0]
                           )
    plt.show()
    z_data = z_map.get_fdata()
    z_data[mask.get_fdata()<1] = 0
    z_map = nib.Nifti1Image(z_data,z_map.affine)
    z_map.to_filename(filename+'.nii')
    newL, newR = volumeToSurface(z_map)
    newL.to_filename(filename+'.L.func.gii')
    newR.to_filename(filename+'.R.func.gii')
    return z_map