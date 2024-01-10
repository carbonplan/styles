<p align="left" >
<a href='https://carbonplan.org'>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://carbonplan-assets.s3.amazonaws.com/monogram/light-small.png">
  <img alt="CarbonPlan monogram." height="48" src="https://carbonplan-assets.s3.amazonaws.com/monogram/dark-small.png">
</picture>
</a>
</p>

# carbonplan / styles

**plot styles for matplotlib and altair**

[![CI](https://github.com/carbonplan/styles/actions/workflows/main.yaml/badge.svg)](https://github.com/carbonplan/styles/actions/workflows/main.yaml)
![PyPI](https://img.shields.io/pypi/v/carbonplan_styles)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A collection of plotting styles for [Matplotlib](https://matplotlib.org/) and [Altair](https://altair-viz.github.io/).

Try it out on Binder:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/carbonplan/styles/main?urlpath=lab)

## install

```shell
pip install "carbonplan[styles]"
```

## usage

There are currently two separate styles/themes available in this package:

1. `carbonplan_dark`: black background, lighter colors
2. `carbonplan_light`: white background, darker colors

Both styels/themes are automatically made available in Matplotlib and Altair.

### matplotlib

```python
from carbonplan import styles

styles.mpl.set_theme(style='carbonplan_dark')
```

### altair

```python
import altair as alt

alt.themes.enable('carbonplan_dark')
```

## license

All the code in this repository is [MIT](https://choosealicense.com/licenses/mit/)-licensed. We include attribution for this content, and we please request that you also maintain that attribution if using this data.

## about us

CarbonPlan is a nonprofit organization that uses data and science for climate action. We aim to improve the transparency and scientific integrity of climate solutions with open data and tools. Find out more at [carbonplan.org](https://carbonplan.org/) or get in touch by [opening an issue](https://github.com/carbonplan/styles/issues/new) or [sending us an email](mailto:hello@carbonplan.org).
