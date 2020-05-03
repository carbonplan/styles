import altair as alt

colors = {
    # from theme.js
    'text': '#ebebec',
    'background': '#1b1e23',
    'primary': '#e4e4e4',
    'secondary': '#808080',
    'muted': '#363a3e',
    'red': '#f07071',
    'orange': '#ea9755',
    'yellow': '#d4c05e',
    'green': '#7eb36a',
    'teal': '#64b9c4',
    'blue': '#85a2f7',
    'purple': '#bc85d9',
    'pink': '#e587b6',
    'grey': '#a9b4c4',
}


def common():
    return {
        'config': {
            'view': {'height': 300, 'width': 400,},
            'mark': {'color': 'dark', 'fill': 'dark'},
        }
    }


def dark():
    c = common()

    return c


def light():
    c = common()

    return c


# register the custom theme under a chosen name
alt.themes.register('carbonplan_dark', dark)
alt.themes.register('carbonplan_light', light)

# enable the newly registered theme
# alt.themes.enable('carbonplan_dark')
