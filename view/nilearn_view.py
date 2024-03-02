import matplotlib.pyplot as plt
from matplotlib import gridspec
from nilearn import plotting
from nilearn.plotting import plot_surf_stat_map,plot_surf_roi
from nilearn.plotting.surf_plotting import _check_views,_check_hemispheres,_get_colorbar_and_data_ranges,_colorbar_from_array
import numpy as np
import itertools
import os
import nibabel as nib
from ..templates import get_surface_file

surf_size = [5124, 10242]
base_dir = os.path.dirname(os.path.abspath(__file__))
def check_hemi(hemispheres):
    pass

def plot_surf_nilearn_single(left_data, right_data, if_roi=False, surf_name = 'fsaverage4',surf_type= 'pial',
                     hemispheres=['left', 'right'], bg_on_data=False,
                     inflate=False, views=['lateral', 'medial'],
                     output_file=None, title=None, colorbar=True, width = 5,
                     vmin=None, vmax=None, threshold=None,overlay_roi = None,
                     symmetric_cbar='auto', cmap='cold_hot', **kwargs):

    plot_func = plot_surf_roi if if_roi is True else plot_surf_stat_map
    surfs = get_surface_file(surf_name)._asdict()[surf_type]
    backgrounds = get_surface_file(surf_name)._asdict()['sulc']
    hemi_nilearn = {'L':'left','R':'right'}
    texture = {
        'L': left_data,
        'R': right_data
    }
    surf_vertex_num = nib.load(surfs['L']).agg_data().squeeze().shape[0]

    modes = _check_views(views)
    hemis = _check_hemispheres(hemispheres)
    if(overlay_roi is not None):
        overlay = {}
        overlay['L'] = overlay_roi[:surf_vertex_num]
        overlay['R'] = overlay_roi[surf_vertex_num:]

    cbar_h = .2
    title_h = .25 * (title is not None)
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

        bg_map = backgrounds[hemi]
        ax = fig.add_subplot(grid[i + len(hemis)], projection="3d")
        axes.append(ax)
        plot_func(
            surfs[hemi],
            texture[hemi],
            view=mode,
            hemi=hemi_nilearn[hemi],
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
                plotting.plot_surf_contours(surfs[hemi], overlay[hemi],
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


def plot_surf_nilearn_row(left_data, right_data, if_roi = False, surf_name = 'fsaverage4',
                     hemispheres = ['L', 'R'], bg_on_data=False, surf_type= 'pial',
                     inflated = False, views=['lateral', 'medial'], title_fontsize = 5,
                     output_file = None, title=None, colorbar=True, width = 5, colorbar_location = 'right',
                     vmin=None, vmax=None, threshold=None,overlay_roi = None,
                     symmetric_cbar='auto', cmap='cold_hot', **kwargs):
    
    plot_func = plot_surf_roi if if_roi is True else plot_surf_stat_map
    surfs = get_surface_file(surf_name)._asdict()[surf_type]
    backgrounds = get_surface_file(surf_name)._asdict()['sulc']
    hemi_nilearn = {'L':'left','R':'right'}
    surf_vertex_num = nib.load(surfs['L']).agg_data().squeeze().shape[0]
    if(overlay_roi is not None):
        overlay = {}
        overlay['L'] = overlay_roi[:surf_vertex_num]
        overlay['R'] = overlay_roi[surf_vertex_num:]

    if(isinstance(left_data,list)):
        num_brain = len(left_data)
        texture = [{'L': left, 'R': right} for left,right in zip(left_data,right_data)]
    else:
        num_brain = 1
        texture = [{'L': left_data, 'R': right_data}]

    cbar_w = .1 * (colorbar)
    title_w = .2 * (title is not None)

    h = 1 / (cbar_w + title_w + 1.3 * len(hemispheres)) * width
    fig = plt.figure(figsize=(width, h * num_brain), constrained_layout=False)
    weight_ratios = [title_w] + [1.3]* len(hemispheres) + [cbar_w]
    grid = gridspec.GridSpec(1 * num_brain, len(hemispheres) + 2,
        left=0., right=1., bottom=-0.1, top=1.1,
        width_ratios=weight_ratios, hspace=0.0, wspace=0.0)
    axes = []

    for pt in range(num_brain):
        _, _, vmin, vmax = _get_colorbar_and_data_ranges(
            np.concatenate([texture[pt]['left'],texture[pt]['right']]),
            vmin=vmin,
            vmax=vmax,
            symmetric_cbar=symmetric_cbar,
            symmetric_data_range=False,
        )
        if title is not None:
            ax = fig.add_subplot(grid[pt,0])
            axes.append(ax)
            ax.set_title(title[pt], loc='left', y =0.5, verticalalignment='center', horizontalalignment= 'left', rotation = 'vertical', fontsize=title_fontsize)
            ax.axis('off')
        for i, (hemi,mode) in enumerate(zip(hemispheres,views)):         
            ax = fig.add_subplot(grid[pt,i + 1], projection="3d")
            axes.append(ax)
            plot_func(
                surfs[hemi],
                texture[pt][hemi],
                view=mode,
                hemi=hemi_nilearn[hemi],
                bg_map=backgrounds[hemi],
                bg_on_data=bg_on_data,
                axes=ax,
                colorbar=False,
                vmin=vmin,
                vmax=vmax,
                threshold=threshold,
                cmap=cmap,
                symmetric_cbar=symmetric_cbar,
                **kwargs,
            )
            if(overlay_roi):
                plotting.plot_surf_contours(surfs[hemi], overlay_roi[hemi],
                            axes=ax)
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
            cbar_grid = gridspec.GridSpecFromSubplotSpec(3, 2, grid[pt,i + 2],height_ratios=[0.2,1,0.2])
            cbar_ax = fig.add_subplot(cbar_grid[1,1])
            axes.append(cbar_ax)
            fig.colorbar(sm, cax=cbar_ax, orientation='vertical')
    if output_file is not None:
        fig.savefig(output_file, bbox_inches="tight")
        plt.close(fig)
    else:
        return fig, axes