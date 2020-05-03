from setuptools import find_packages, setup
from setuptools.command.develop import develop
from setuptools.command.install import install
import os
import shutil
import atexit

import matplotlib


def install_mplstyle():
    root = os.path.dirname(__file__)

    for theme in ['carbonplan_dark', 'carbonplan_light']:
        fname = f"{theme}.mplstyle"
        stylefile = os.path.join("carbonplan_styles", "mpl", fname)

        mpl_stylelib_dir = os.path.join(matplotlib.get_configdir(), "stylelib")
        os.makedirs(mpl_stylelib_dir, exist_ok=True)

        src = os.path.join(root, stylefile)
        dst = os.path.join(mpl_stylelib_dir, fname)
        if not os.path.exists(dst):
            print("Installing style into", mpl_stylelib_dir)
            shutil.copy(src, dst)


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        install_mplstyle()

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        install_mplstyle()

setup(
    name='carbonplan-styles',
    version='0.0.1',
    packages=find_packages(exclude=("tests",)),
    package_dir={"carbonplan_styles": "carbonplan_styles"},
    install_requires=['matplotlib', 'altair'],
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand
    }
)