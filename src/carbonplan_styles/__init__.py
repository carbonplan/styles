import json
from importlib.metadata import PackageNotFoundError, version
from importlib.resources import files
from typing import Literal

import matplotlib as mpl
from cycler import cycler
from matplotlib.colors import ListedColormap

from . import colors

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "0.0.0+dev"

PALETTE = ["blue", "orange", "green", "red", "purple", "pink", "grey", "yellow", "teal"]

cmaps: dict[str, ListedColormap] = {}
for _k, _v in json.loads(
    files(__name__).joinpath("colormaps.json").read_text()
).items():
    _cmap = ListedColormap(_v, name=_k.replace("-", "_"))
    for _c in (_cmap, _cmap.reversed()):
        cmaps[_c.name] = _c
        mpl.colormaps.register(_c, force=True)


def style(mode: Literal["light", "dark"] = "dark") -> dict:
    """CarbonPlan matplotlib rcParams for `mode`."""
    if mode not in ("light", "dark"):
        raise ValueError(f"mode must be 'light' or 'dark', got {mode!r}")
    c = getattr(colors, mode)
    return {
        "axes.facecolor": c["background"],
        "axes.edgecolor": c["muted"],
        "axes.labelcolor": c["secondary"],
        "axes.titlecolor": c["text"],
        "axes.grid": False,
        "axes.axisbelow": True,
        "axes.spines.right": False,
        "axes.spines.top": False,
        "axes.prop_cycle": cycler(color=[c[k] for k in PALETTE]),
        "figure.facecolor": c["background"],
        "savefig.facecolor": c["background"],
        "grid.color": c["muted"],
        "text.color": c["text"],
        "xtick.color": c["muted"],
        "ytick.color": c["muted"],
        "xtick.labelcolor": c["secondary"],
        "ytick.labelcolor": c["secondary"],
        "legend.frameon": False,
        "lines.solid_capstyle": "round",
        "lines.markeredgewidth": 0.0,
        "patch.edgecolor": c["background"],
        "patch.force_edgecolor": True,
        "image.cmap": f"cool_{mode}",
        "font.family": "monospace",
        "font.monospace": [
            "relative-mono-11-pitch-pro",
            "Space Mono",
            "Menlo",
            "DejaVu Sans Mono",
            "monospace",
        ],
    }


def set_theme(mode: Literal["light", "dark"] = "dark", rc: dict | None = None) -> None:
    """Apply the CarbonPlan theme to matplotlib (and xarray.plot, if installed).

    `rc` overrides any matplotlib rcParam, e.g. ``set_theme("dark", rc={"font.size": 12})``.
    """
    mpl.rcParams.update(style(mode) | (rc or {}))
    try:
        import xarray as xr
    except ImportError:
        return
    # xarray ignores image.cmap and uses its own defaults
    xr.set_options(cmap_sequential=f"cool_{mode}", cmap_divergent=f"orangeblue_{mode}")
