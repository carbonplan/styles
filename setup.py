import os

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")


if os.path.exists("README.md"):
    with open("README.md") as f:
        long_description = f.read()
else:
    long_description = ""


CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Intended Audience :: Science/Research",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Topic :: Scientific/Engineering",
]

ENTRY_POINTS = {
    "altair.vegalite.v4.theme": [
        "carbonplan_dark = carbonplan_styles.altair:dark",
        "carbonplan_light = carbonplan_styles.altair:light",
    ],
}


setup(
    name="carbonplan-styles",
    description="CarbonPlan plotting styles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    maintainer="CarbonPlan",
    maintainer_email="tech@carbonplan.org",
    url="https://github.com/carbonplan/styles",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    entry_points=ENTRY_POINTS,
    install_requires=install_requires,
    keywords=["matplotlib", "altair"],
    classifiers=CLASSIFIERS,
    use_scm_version={"version_scheme": "post-release", "local_scheme": "dirty-tag"},
    setup_requires=["setuptools_scm", "setuptools>=30.3.0"],
)
