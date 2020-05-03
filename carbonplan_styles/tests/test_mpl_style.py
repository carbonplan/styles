import matplotlib.pyplot as plt
import pytest


@pytest.mark.parametrize('style', ['carbonplan_dark', 'carbonplan_light'])
def test_set_style(style):
    assert style in plt.style.available
    assert plt.style.use(style) is None
