dark = {
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

light = {
    'text': '#1b1e23',
    'background': '#FFFFFF',
    'primary': '#1b1e23',
    'secondary': '#808080',
    'muted': '#b0afb1',
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


def colors(mode='dark'):
    if mode in ['dark', 'carbonplan_dark']:
        c = dark
    elif mode in ['light', 'carbonplan_light']:
        c = light
    else:
        raise ValueError('unknown color mode %s' % mode)
    return c


def tags(mode='dark'):

    c = colors(mode=mode)

    return (
        {
            'mineralization': c['grey'],
            'soil': c['orange'],
            'biomass': c['yellow'],
            'forests': c['green'],
            'ocean': c['teal'],
            'dac': c['purple'],
            'biochar': c['yellow'],
            'materials': c['yellow'],
            'broker': c['grey'],
            'beccs': c['yellow'],
            'reforestation': c['green'],
            'avoided conversion': c['green'],
            'agroforestry': c['green'],
            'burial': c['yellow'],
            'phytoplankton': c['teal'],
            'injection': c['grey'],
        },
    )
