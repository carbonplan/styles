import warnings

import matplotlib as mpl
import matplotlib.colors as mcolors
import numpy as np
import seaborn as sns

from ..colors import colors, hex_to_rgb, rgb_to_dec
from . import colormaps  # noqa

palette_colors = ['blue', 'orange', 'green', 'red', 'purple', 'pink', 'grey', 'yellow', 'teal']


def get_style_config(mode):

    c = colors(mode=mode)

    if mode == 'light':
        background = 'white'  # instead of c['background']
    else:
        background = c['background']

    style = {
        'axes.facecolor': background,
        'axes.edgecolor': c['secondary'],
        'axes.grid': False,
        'axes.axisbelow': True,
        'axes.labelcolor': c['text'],
        'figure.facecolor': background,
        'grid.color': c['secondary'],
        'grid.linestyle': '-',
        'text.color': c['text'],
        'xtick.color': c['secondary'],
        'ytick.color': c['secondary'],
        'xtick.labelcolor': c['blue'],
        'ytick.labelcolor': c['blue'],
        'xtick.direction': 'out',
        'ytick.direction': 'out',
        'lines.markeredgewidth': 0.0,
        'lines.solid_capstyle': 'round',
        'patch.edgecolor': c['secondary'],
        'patch.force_edgecolor': True,
        'image.cmap': 'cool_light',
        'font.weight': '400',
        'font.family': 'monospace',
        'font.monospace': ['relative-mono-11-pitch-pro', 'Menlo', 'monospace'],
        'font.sans-serif': [
            'relative-book-pro',
            'Roboto',
            'system-ui',
            '-apple-system',
            'BlinkMacSystemFont',
        ],
        'xtick.bottom': True,
        'xtick.top': False,
        'ytick.left': True,
        'ytick.right': False,
        'axes.spines.left': True,
        'axes.spines.bottom': True,
        'axes.spines.right': False,
        'axes.spines.top': False,
        'scatter.marker': 'o',
        'scatter.edgecolors': None,
    }

    return style, c


def set_theme(
    context='notebook', style='carbonplan_light', font='monospace', font_scale=1, rc=None
):
    """Set multiple theme parameters in one step.

    Each set of parameters can be set directly or temporarily, see the
    referenced functions below for more information.

    Parameters
    ----------
    context : string or dict
        Plotting context parameters, see :func:`plotting_context`.
    style : string or dict
        Axes style parameters, see :func:`axes_style`.
    font : string
        Font family, see matplotlib font manager.
    rc : dict or None
        Dictionary of rc parameter mappings to override the above.

    See Also
    --------
    seaborn.set_theme
    """
    # set context
    sns.set_context(context, font_scale)

    # set style
    style_dict, colors_dict = get_style_config(style)
    sns.set_style(style_dict, rc={'font.family': font})

    # set color palette
    c = [colors_dict[k] for k in palette_colors]
    palette = sns.color_palette(c)
    sns.set_palette(palette)

    if rc is not None:
        mpl.rcParams.update(rc)


def get_continuous_cmap(hex_list, float_list=None, name=None):
    """
    Creates and returns a color map that can be used in heat map figures.
    If float_list is not provided, colour map graduates linearly between each color in hex_list.
    If float_list is provided, each color in hex_list is mapped to the respective location in float_list.

    Parameters
    ----------
    hex_list : list
        Hex code strings
    float_list: list, optional
        List of floats between 0 and 1, same length as hex_list. Must start with 0 and end with 1.

    Returns
    ----------
    cmap : mcolors.LinearSegmentedColormap

    References
    ----------
    https://towardsdatascience.com/beautiful-custom-colormaps-with-matplotlib-5bab3d1f0e72
    """

    warnings.warn(
        'get_continuous_cmap is deprecated, use carbonplan_styles.mpl.colormaps instead',
        DeprecationWarning,
    )

    if name is None:
        name = '-'.join(hex_list)

    rgb_list = [rgb_to_dec(hex_to_rgb(i)) for i in hex_list]

    if float_list:
        pass
    else:
        float_list = list(np.linspace(0, 1, len(rgb_list)))

    cdict = dict()
    for num, col in enumerate(['red', 'green', 'blue']):
        cdict[col] = [
            [float_list[i], rgb_list[i][num], rgb_list[i][num]] for i in range(len(float_list))
        ]
    cmap = mcolors.LinearSegmentedColormap(name, segmentdata=cdict, N=256)

    return cmap


def get_colormap(name):

    warnings.warn(
        'get_colormap is deprecated, use carbonplan_styles.mpl.colormaps instead',
        DeprecationWarning,
    )

    if name == 'blues':
        return get_continuous_cmap(['#CFE0F9', '#588EF9', '#0432A5'])
    elif name == 'pinks':
        return get_continuous_cmap(['#F9C7ED', '#E563BA', '#770361'])
    elif name == 'reds':
        return get_continuous_cmap(['#F9D3BD', '#E87A3D', '#752003'])
