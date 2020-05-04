font = 'relative-faux-book-pro, Roboto, system-ui, -apple-system, BlinkMacSystemFont'
labelfont = 'relative-faux-book-pro, Roboto, system-ui, -apple-system, BlinkMacSystemFont'
sourcefont = 'relative-faux-book-pro, Roboto, system-ui, -apple-system, BlinkMacSystemFont'


def colors(mode='dark'):
    if mode == 'dark':
        colors = {
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
    elif mode == 'light':
        colors = {
            'text': '#333333',
            'background': '#ebebec',
            'primary': '#484848',
            'secondary': '#b0b0b0',
            'muted': 'rgb(200,200,200)',
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
    else:
        raise ValueError(mode)
    return colors
