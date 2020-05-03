import altair as alt
import pytest

import carbonplan_styles.altair  # noqa: F401


@pytest.mark.parametrize('theme', ['carbonplan_dark', 'carbonplan_light'])
def test_enable_theme(theme):
    assert theme in alt.themes.names()
    assert alt.themes.enable(theme)
