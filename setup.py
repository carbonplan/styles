import os
import shutil

import matplotlib
from setuptools import find_packages, setup
from setuptools.command.develop import develop
from setuptools.command.install import install

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')


if os.path.exists('README.md'):
    with open('README.md') as f:
        long_description = f.read()
else:
    long_description = ''


def install_mplstyle():
    root = os.path.dirname(__file__)

    for theme in ['carbonplan_dark', 'carbonplan_light']:
        fname = f'{theme}.mplstyle'
        stylefile = os.path.join('carbonplan_styles', 'mpl', fname)

        mpl_stylelib_dir = os.path.join(matplotlib.get_configdir(), 'stylelib')
        os.makedirs(mpl_stylelib_dir, exist_ok=True)

        src = os.path.join(root, stylefile)
        dst = os.path.join(mpl_stylelib_dir, fname)
        if not os.path.exists(dst):
            print('Installing style into', mpl_stylelib_dir)
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


CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Scientific/Engineering',
]


setup(
    name='carbonplan-styles',
    description='CarbonPlan plotting styles',
    long_description=long_description,
    python_requires='>=3.6',
    maintainer='Joe Hamman',
    maintainer_email='joe@carbonplan.org',
    url='https://github.com/carbonplan/carbonplan_styles',
    license='MIT',
    packages=find_packages(exclude=('tests',)),
    package_dir={'carbonplan_styles': 'carbonplan_styles'},
    install_requires=install_requires,
    keywords=['matplotlib', 'altair'],
    classifiers=CLASSIFIERS,
    use_scm_version={'version_scheme': 'post-release', 'local_scheme': 'dirty-tag'},
    setup_requires=['setuptools_scm', 'setuptools>=30.3.0'],
    cmdclass={'develop': PostDevelopCommand, 'install': PostInstallCommand},
)
