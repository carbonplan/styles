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
        return dark
    elif mode in ['light', 'carbonplan_light']:
        return light
    else:
        raise ValueError('unknown color mode %s' % mode)


def hex_to_rgb(hex):
    """
    Converts hex to rgb colours

    Parameters
    ----------
    hex : string
        6 characters representing a hex color

    Returns
    -------
    rgb : tuple (length 3)
        RGB values

    References
    ----------
    https://towardsdatascience.com/beautiful-custom-colormaps-with-matplotlib-5bab3d1f0e72
    """
    hex = hex.strip('#')  # removes hash symbol if present
    lv = len(hex)

    return tuple(int(hex[i : i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_dec(value):
    """
    Converts rgb to decimal colours (i.e. divides each value by 256)

    Parameters
    ----------
    value: tuple (length 3)
        RGB values

    Returns
    -------
    dec : tuple (length 3)
        Decimal color values

    References
    ----------
    https://towardsdatascience.com/beautiful-custom-colormaps-with-matplotlib-5bab3d1f0e72
    """
    return tuple(v / 256 for v in value)
