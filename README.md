# CarbonPlan Styles

A collection of plotting styles for Matplotlib[https://matplotlib.org/] and Altair[https://altair-viz.github.io/].

![CI](https://github.com/jhamman/carbonplan-styles/workflows/CI/badge.svg)

## Install

```
pip install git://github.com/jhamman/carbonplan-styles.git
```

## Usage

There are currently two separate styles/themes available in this package:

1. `carbonplan_dark`: black background, lighter colors
2. `carbonplan_light`: white background, darker colors

Both styels/themes are automatically made available in Matplotlib and Altair

#### Matplotlib

```python
plt.style.use('carbonplan_dark')
```

_Note: The install of this package adds Matplotlib style sheets to `~/.config/matplotlib`. This will only happen once and future updates will need to be done manually._

#### Altair

```python
alt.themes.enable('carbonplan_dark')
```
