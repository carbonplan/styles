import matplotlib.pyplot as plt
import pytest

import carbonplan_styles.mpl


@pytest.mark.parametrize('style', ['carbonplan_dark', 'carbonplan_light'])
def test_set_style(style):
    assert style in plt.style.available
    assert plt.style.use(style) is None


@pytest.mark.parametrize('style', ['dark', 'light'])
def test_set_style_from_dict(style):

    style_obj = getattr(carbonplan_styles.mpl, style)
    assert style_obj
    assert plt.style.use(style_obj) is None
