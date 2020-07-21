import os

import matplotlib

from carbonplan_styles import colors


def make_style_dict(mode):

    hex_colors = colors(mode)
    temp_colors = {k: v.strip('#') for k, v in hex_colors.items()}

    style_dict = {
        'figure.facecolor': temp_colors['background'],
        'text.color': temp_colors['text'],
        'axes.labelcolor': temp_colors['text'],
        'legend.frameon': False,
        'legend.numpoints': 1,
        'legend.scatterpoints': 1,
        'xtick.direction': 'out',
        'ytick.direction': 'out',
        'xtick.color': temp_colors['text'],
        'ytick.color': temp_colors['text'],
        'axes.axisbelow': True,
        'image.cmap': 'Greys',
        'font.family': 'monospace',
        'font.monospace': temp_colors['text'],
        'grid.linestyle': '-',
        'axes.grid': False,
        'axes.facecolor': temp_colors['background'],
        'axes.edgecolor': temp_colors['text'],
        'axes.linewidth': 0,
        'grid.color': temp_colors['text'],
        'xtick.major.size': 0,
        'ytick.major.size': 0,
        'xtick.minor.size': 0,
        'ytick.minor.size': 0,
    }

    return style_dict


def make_theme(mode):
    style = make_style_dict(mode)
    theme = '\n'.join(['# CarbonPlan styles'] + [f'{k}: {v}' for k, v in style.items()])
    return theme


def install(mpl_stylelib_dir=None):
    if mpl_stylelib_dir is None:
        mpl_stylelib_dir = os.path.join(matplotlib.get_configdir(), 'stylelib')

    for mode in ['dark', 'light']:
        theme = make_theme(mode)
        fname = os.path.join(mpl_stylelib_dir, f'{mode}.mplstyle')
        print(f'writing {mode} to {fname}.')
        with open(fname, 'w') as f:
            f.write(theme)


if __name__ == '__main__':

    for mode in ['dark', 'light']:
        theme = make_theme(mode)
        with open(f'carbonplan_styles/mpl/carbonplan_{mode}.mplstyle', 'w') as f:
            f.write(theme)
