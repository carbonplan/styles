import pytest

from carbonplan_styles.mpl import set_theme


@pytest.mark.parametrize('style', ['carbonplan_dark', 'carbonplan_light'])
def test_set_style(style):
    set_theme(style=style)
