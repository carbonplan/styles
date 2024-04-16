import functools
import json
import pathlib

from matplotlib.cm import register_cmap
from matplotlib.colors import ListedColormap

mod_dir = pathlib.Path(__file__).parent.parent


@functools.lru_cache
def colormaps():
    """return a dictionary of colormaps"""

    with open(mod_dir / "data" / "colormaps.json") as f:
        data = json.load(f)

    cmaps = {}
    for k, v in data.items():
        key = k.replace("-", "_")
        cmaps[key] = ListedColormap(v, name=key)

        key_r = key + "_r"
        cmaps[key_r] = cmaps[key].reversed()

    return cmaps


# register colormaps in this namespace
_cmaps = colormaps()

lcs = locals()
lcs.update(**_cmaps)

# register colormaps in the matplotlib namespace
for k, v in _cmaps.items():
    register_cmap(name=v.name, cmap=v)
