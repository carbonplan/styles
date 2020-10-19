import matplotlib as mpl
import seaborn as sns

from .colors import colors

palette_colors = ['blue', 'orange', 'green', 'red', 'purple', 'pink', 'grey', 'yellow', 'teal']


def get_style_dict(c):

    style = {
        'axes.facecolor': c['background'],
        'axes.edgecolor': c['secondary'],
        'axes.grid': False,
        'axes.axisbelow': True,
        'axes.labelcolor': c['text'],
        'figure.facecolor': c['background'],
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
        'image.cmap': 'rocket',
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

    return style


def set_theme(context='notebook', style='carbonplan_dark', font='monospace', font_scale=1, rc=None):
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

    # get carbonplan colors
    colors_dict = colors(mode=style)

    # set style
    style_dict = get_style_dict(colors_dict)
    sns.set_style(style_dict, rc={'font.family': font})

    # set color palette
    c = [colors_dict[k] for k in palette_colors]
    palette = sns.color_palette(c)
    sns.set_palette(palette)

    if rc is not None:
        mpl.rcParams.update(rc)
