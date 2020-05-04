from carbonplan_styles import colors, font

template = '''# CarbonPlan styles
figure.facecolor: {background}
text.color: {text}
axes.labelcolor: {text}
legend.frameon: False
legend.numpoints: 1
legend.scatterpoints: 1
xtick.direction: out
ytick.direction: out
xtick.color: {text}
ytick.color: {text}
axes.axisbelow: True
image.cmap: Greys
font.family: sans-serif
font.sans-serif: font
grid.linestyle: -
axes.grid: False
axes.facecolor: {background}
axes.edgecolor: {text}
axes.linewidth: 0
grid.color: {text}
xtick.major.size: 0
ytick.major.size: 0
xtick.minor.size: 0
ytick.minor.size: 0
'''


def make_theme(mode):
    hex_colors = colors(mode)
    temp_colors = {k: v.strip('#') for k, v in hex_colors.items()}
    return template.format(**temp_colors)


if __name__ == '__main__':

    for mode in ['dark', 'light']:
        theme = make_theme(mode)
        with open(f'carbonplan_styles/mpl/carbonplan_{mode}.mplstyle', 'w') as f:
            f.write(theme)
