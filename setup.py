import re

from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("README.md", "r") as f:
    long_description = f.read()

with open("arts/__init__.py", "r") as f:
    vf = f.read()

version = re.search(r"^_*version_* = ['\"]([^'\"]*)['\"]", vf, re.M).group(1)

setup(
    name="arts",
    version=version,
    packages=find_packages(),
    url="https://github.com/thepetabyteproject/arts",
    author="TPP People",
    # scripts=glob.glob("bin/*"),
    tests_require=["pytest"],  # , "pytest-cov"],
    install_requires=required,
    long_description=long_description,
    long_description_content_type="text/markdown",
    # author_email="",
    zip_safe=False,
    description="Accurate Radio Transient Statistics",
    classifiers=[
        "Natural Language :: English",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
)
