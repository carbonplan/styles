import pytest
from carbonplan import styles


@pytest.mark.parametrize('style', ['carbonplan_dark', 'carbonplan_light'])
def test_set_style(style):
    styles.mpl.set_theme(style=style)
