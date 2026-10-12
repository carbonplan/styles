import json
from importlib.resources import files

import matplotlib as mpl
import pytest

import carbonplan_styles as cps


@pytest.fixture(autouse=True)
def _reset_rc():
    with mpl.rc_context():
        yield


@pytest.mark.parametrize("mode", ["light", "dark"])
def test_set_theme(mode):
    cps.set_theme(mode, rc={"font.size": 13})
    c = getattr(cps.colors, mode)
    assert mpl.colors.same_color(mpl.rcParams["axes.facecolor"], c["background"])
    assert mpl.rcParams["axes.prop_cycle"].by_key()["color"][0] == c["blue"]
    assert mpl.rcParams["image.cmap"] == f"cool_{mode}"
    assert mpl.rcParams["font.size"] == 13


def test_bad_mode():
    with pytest.raises(ValueError):
        cps.set_theme("blue")
    with pytest.raises(ValueError):
        cps.style("drak")


def test_neutrals():
    assert cps.colors.chalk == cps.colors.dark["text"] == cps.colors.dark["primary"]
    assert cps.colors.carbon == cps.colors.dark["background"]


def test_colormaps():
    names = json.loads(
        files("carbonplan_styles").joinpath("colormaps.json").read_text()
    )
    for k in names:
        for name in (k.replace("-", "_"), k.replace("-", "_") + "_r"):
            assert cps.cmaps[name].name == name
            assert mpl.colormaps[name] == cps.cmaps[name]


def test_default_dark():
    cps.set_theme()
    assert mpl.colors.same_color(
        mpl.rcParams["axes.facecolor"], cps.colors.dark["background"]
    )


def test_xarray():
    xr = pytest.importorskip("xarray")
    cps.set_theme("dark")
    assert xr.get_options()["cmap_sequential"] == "cool_dark"
    assert xr.get_options()["cmap_divergent"] == "orangeblue_dark"
