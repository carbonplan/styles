import functools
import json
import pathlib

from matplotlib.cm import register_cmap
from matplotlib.colors import ListedColormap

mod_dir = pathlib.Path(__file__).parent.parent


@functools.lru_cache
def colormaps():

    with open(mod_dir / 'data' / 'colormaps.json', mode='r') as f:
        data = json.load(f)

    cmaps = {}
    for k, v in data.items():
        key = k.replace('-', '_')
        cmaps[key] = ListedColormap(v, name=key)

        key_r = key + '_r'
        cmaps[key_r] = cmaps[key].reversed()

    return cmaps


_cmaps = colormaps()

lcs = locals()
lcs.update(**_cmaps)

for k, v in _cmaps.items():
    register_cmap(name=v.name, cmap=v)
