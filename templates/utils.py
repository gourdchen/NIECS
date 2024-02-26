import os
from neuromaps.datasets import fetch_fsaverage,fetch_fslr
from collections import namedtuple

base_dir = os.path.dirname(os.path.abspath(__file__))
def get_surface_file(name: str) -> namedtuple:
    '''
    Parameters
    ----------
    name : 
        surface template name, ['fsaverage4','fsaverage5','fsaverage','fsLR_32k']
    Returns
    -------
    suface namedtuple
    - white, pial, inflated, sphere, medial, sulc, vaavg
    -- L
    -- R
    '''
    surface_size = {'fsaverage4':'3k','fsaverage5':'10k','fsaverage':'41k', 'fsLR_32k':'32k'}
    surface_get_func = {'fsaverage4': fetch_fsaverage,'fsaverage5': fetch_fsaverage,'fsaverage': fetch_fsaverage,'fsLR_32k': fetch_fslr}
    surfs = surface_get_func[name](surface_size[name],data_dir=base_dir + '/data/')
    return surfs