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

Matplotlib sytle sheets are installed automatically.

```python
plt.style.use('carbonplan_dark')
```

We're still working out Altair's automatic entrypoints system. In the meantime, activation requires importing this library:

```python
import carbonplan_styles.altair
```
