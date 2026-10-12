<p align="left" >
<a href='https://carbonplan.org'>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://carbonplan-assets.s3.amazonaws.com/monogram/light-small.png">
  <img alt="CarbonPlan monogram." height="48" src="https://carbonplan-assets.s3.amazonaws.com/monogram/dark-small.png">
</picture>
</a>
</p>

# carbonplan / styles

**plot styles for matplotlib and xarray**

[![CI](https://github.com/carbonplan/styles/actions/workflows/ci.yml/badge.svg)](https://github.com/carbonplan/styles/actions/workflows/ci.yml)
![PyPI](https://img.shields.io/pypi/v/carbonplan_styles)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

CarbonPlan colors, colormaps, and a one-line theme for [Matplotlib](https://matplotlib.org/) and [xarray](https://docs.xarray.dev/) plotting.

## install

```shell
uv add carbonplan-styles   # or: pip install carbonplan-styles
```

## usage

```python
import carbonplan_styles as cps

cps.set_theme()  # dark (default)
cps.set_theme("light")  # light
```

This updates matplotlib `rcParams` (colors, color cycle, fonts, spines, default colormap) and, if xarray is installed, xarray's default sequential and divergent colormaps. Anything else plotted through matplotlib (pandas, xarray, etc.) picks it up.

Override any rcParam:

```python
cps.set_theme("dark", rc={"font.size": 12, "axes.grid": True})
```

Use temporarily:

```python
import matplotlib.pyplot as plt

with plt.style.context(cps.style("dark")):
    ...
```

### colors and colormaps

```python
cps.colors.light["blue"]  # palette dicts: cps.colors.light / cps.colors.dark
cps.colors.chalk, cps.colors.carbon  # brand neutrals: "#ebebec", "#1b1e23"
cps.cmaps["warm_light"]  # all colormaps, also registered by name in matplotlib
da.plot(cmap="redteal_dark")
```

Colormaps: `reds oranges yellows greens teals blues purples pinks greys fire earth water heart wind warm cool pinkgreen redteal orangeblue yellowpurple redgrey orangegrey yellowgrey greengrey tealgrey bluegrey purplegrey pinkgrey rainbow sinebow`, each with `_light` / `_dark` variants and `_r` reversals.

### upgrading from 0.5

0.6 drops altair and seaborn support and flattens the API:

| 0.5 | 0.6 |
| --- | --- |
| `cps.mpl.set_theme(style="carbonplan_dark")` | `cps.set_theme("dark")` |
| `cps.colors.colors("dark")` | `cps.colors.dark` |
| `cps.mpl.colormaps()` | `cps.cmaps` |
| `cps.version` | `cps.__version__` |
| `cps.altair` | removed |
| Python >= 3.10 | Python >= 3.12 |

Plots also look slightly different: tick labels are grey instead of blue, axes edges are lower contrast, and bar/patch edges match the background.

## development

```shell
uv sync
uv run pytest
uv run prek install        # ruff on commit
uv run prek run --all-files
uv run ty check src/
```

Release: bump `version` in `pyproject.toml`, then push a `v*` tag.

## license

All the code in this repository is [MIT](https://choosealicense.com/licenses/mit/)-licensed.

## about us

CarbonPlan is a nonprofit organization that uses data and science for climate action. We aim to improve the transparency and scientific integrity of climate solutions with open data and tools. Find out more at [carbonplan.org](https://carbonplan.org/) or get in touch by [opening an issue](https://github.com/carbonplan/styles/issues/new) or [sending us an email](mailto:hello@carbonplan.org).
