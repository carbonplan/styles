from importlib.metadata import PackageNotFoundError as _PackageNotFoundError
from importlib.metadata import version as _version

from . import altair, colors, mpl  # noqa

try:
    version = _version(__name__)
except _PackageNotFoundError:
    # package is not installed
    version = "unknown"
__version__ = version


banner = """-------------------------------
   ███        ███        ███
  ██          ███          ██
 ██           ███           ██
 ██      ██   ███   ██      ██
 ██       ███ ███ ███       ██
  ██         █████         ██
   ███        ███        ███

/ (carbon)plan
/ carbonplan.org
/ https://github.com/carbonplan
-------------------------------
"""
