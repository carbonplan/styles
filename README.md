<img
  src='https://carbonplan-assets.s3.amazonaws.com/monogram/dark-small.png'
  height='48'
/>

# carbonplan / styles

**plot styles for matplotlib and altair**

[![GitHub][github-badge]][github]
[![Build Status]][actions]
[![codecov](https://codecov.io/gh/carbonplan/styles/branch/main/graph/badge.svg?token=NCBBIS7AJE)](https://codecov.io/gh/carbonplan/styles)
![MIT License][]

[github]: https://github.com/carbonplan/styles
[github-badge]: https://badgen.net/badge/-/github?icon=github&label
[build status]: https://github.com/carbonplan/styles/actions/workflows/main.yaml/badge.svg
[actions]: https://github.com/carbonplan/styles/actions/workflows/main.yaml
[mit license]: https://badgen.net/badge/license/MIT/blue

A collection of plotting styles for [Matplotlib](https://matplotlib.org/) and [Altair](https://altair-viz.github.io/).

Try it out on Binder:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jhamman/carbonplan-styles/master?urlpath=lab)

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

All the code in this repository is [MIT](https://choosealicense.com/licenses/mit/) licensed. We include attribution for this content, and we please request that you also maintain that attribution if using this data.

## about us

CarbonPlan is a non-profit organization that uses data and science for climate action. We aim to improve the transparency and scientific integrity of carbon removal and climate solutions through open data and tools. Find out more at [carbonplan.org](https://carbonplan.org/) or get in touch by [opening an issue](https://github.com/carbonplan/styles/issues/new) or [sending us an email](mailto:hello@carbonplan.org).
