from matplotlib import gridspec
from nilearn.plotting import plot_surf_stat_map,plot_surf_roi
from nilearn.plotting.surf_plotting import _check_views,_check_hemispheres,_get_colorbar_and_data_ranges,_colorbar_from_array
import itertools
import os
from ..templates import get_surface_file

surf_size = [5124, 10242,]
                      
def plot_surf_nilearn(left_data, right_data, if_roi=False, surf_name = 'fsaverage4',
                     hemispheres=['left', 'right'], bg_on_data=False,
                     inflate=False, views=['lateral', 'medial'],
                     output_file=None, title=None, colorbar=True, width = 5,
                     vmin=None, vmax=None, threshold=None,overlay_roi = None,
                     symmetric_cbar='auto', cmap='cold_hot', **kwargs):
    for arg in ("figure", "axes", "engine"):
        if arg in kwargs:
            raise ValueError(
                'plot_img_on_surf does not accept '
                f'{arg} as an argument')
    base_dir = os.path.dirname(os.path.abspath(__file__))
    surfs = get_surface_file(surf_name)
    
    modes = _check_views(views)
    hemis = _check_hemispheres(hemispheres)

        
    if(overlay_roi is not None):
        overlay = {}
        overlay['left'] = overlay_roi[:2562]
        overlay['right'] = overlay_roi[2562:]

    cbar_h = .2
    title_h = .25 * (title is not None)
    #w, h = plt.figaspect()
    h = width * (len(modes) + cbar_h + title_h) / len(hemispheres)
    fig = plt.figure(figsize=(width, h), constrained_layout=False)
    height_ratios = [title_h] + [1.] * len(modes) + [cbar_h]
    grid = gridspec.GridSpec(
        len(modes) + 2, len(hemis),
        left=0., right=1., bottom=0., top=1.,
        height_ratios=height_ratios, hspace=0.0, wspace=0.0)
    axes = []

    # get vmin and vmax for entire data (all hemis)
    _, _, vmin, vmax = _get_colorbar_and_data_ranges(
        np.concatenate([left_data,right_data]),
        vmin=vmin,
        vmax=vmax,
        symmetric_cbar=symmetric_cbar,
        symmetric_data_range=False,
    )
    if(not if_roi):
        plot_func = plot_surf_stat_map
    else:
        plot_func = plot_surf_roi
    for i, (mode, hemi) in enumerate(itertools.product(modes, hemis)):

        curv_map = surface.load_surf_data(surf_mesh[f"curv_{hemi}"])
        bg_map = curv_map
        ax = fig.add_subplot(grid[i + len(hemis)], projection="3d")
        axes.append(ax)

        plot_func(
            surf[hemi],
            texture[hemi],
            view=mode,
            hemi=hemi,
            bg_map=bg_map,
            bg_on_data=bg_on_data,
            axes=ax,
            colorbar=False,  # Colorbar created externally.
            vmin=vmin,
            vmax=vmax,
            threshold=threshold,
            cmap=cmap,
            symmetric_cbar=symmetric_cbar,
            **kwargs,
        )
        if(overlay_roi is not None):
                plotting.plot_surf_contours(surf[hemi], overlay[hemi],
                            axes=ax, levels=[1], colors=['black'])
        ax.set_box_aspect(None, zoom=1.5)

    if colorbar:
        sm = _colorbar_from_array(
            left_data,
            vmin,
            vmax,
            threshold,
            symmetric_cbar=symmetric_cbar,
            cmap=plt.get_cmap(cmap),
        )

        cbar_grid = gridspec.GridSpecFromSubplotSpec(3, 3, grid[-1, :])
        cbar_ax = fig.add_subplot(cbar_grid[1])
        axes.append(cbar_ax)
        fig.colorbar(sm, cax=cbar_ax, orientation='horizontal')
    if title is not None:
        fig.suptitle(title, y=1. - title_h / sum(height_ratios), va="bottom")

    if output_file is not None:
        fig.savefig(output_file, bbox_inches="tight")
        plt.close(fig)
    else:
        return fig, axes