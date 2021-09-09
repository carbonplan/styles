import itertools

import pytest
from matplotlib import cm
from matplotlib.colors import ListedColormap

from carbonplan_styles.mpl import colormaps, set_theme


@pytest.mark.parametrize('style', ['carbonplan_dark', 'carbonplan_light'])
def test_set_style(style):
    set_theme(style=style)


def test_colormaps():
    base_names = [
        'reds',
        'oranges',
        'yellows',
        'greens',
        'teals',
        'blues',
        'purples',
        'pinks',
        'greys',
        'fire',
        'earth',
        'water',
        'heart',
        'wind',
        'warm',
        'cool',
        'pinkgreen',
        'redteal',
        'orangeblue',
        'yellowpurple',
        'redgrey',
        'orangegrey',
        'yellowgrey',
        'greengrey',
        'tealgrey',
        'bluegrey',
        'purplegrey',
        'pinkgrey',
        'rainbow',
        'sinebow',
    ]

    explicit_cmaps = colormaps.colormaps()

    for pieces in itertools.product(base_names, ['_light', '_dark'], '', '_r'):
        cmap_name = ''.join(pieces)

        exp_camp = explicit_cmaps[cmap_name]
        assert isinstance(exp_camp, ListedColormap)

        imp_cmap = getattr(colormaps, cmap_name)
        assert isinstance(imp_cmap, ListedColormap)

        mpl_cmap = cm.get_cmap(cmap_name)
        assert isinstance(mpl_cmap, ListedColormap)

        assert exp_camp.colors == imp_cmap.colors
        assert exp_camp.name == imp_cmap.name
        assert exp_camp.colors == mpl_cmap.colors
        assert exp_camp.name == mpl_cmap.name
