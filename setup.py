 #!/usr/bin/env python
# import os
# import sys

from setuptools import setup, find_packages

MAJOR = 0
MINOR = 0
MICRO = 1
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)
QUALIFIER = ''


DISTNAME = 'climate_index'
LICENSE = 'BSD'
AUTHOR = 'Wenchang Yang'
AUTHOR_EMAIL = 'yang.wenchang@uci.edu'
URL = 'https://github.com/wy2136/climate_index'
CLASSIFIERS = []

INSTALL_REQUIRES = ['pandas >= 0.15.0']


DESCRIPTION = "Download and visulize climate indices from NOAA website."
LONG_DESCRIPTION = """
Major APIs:

print_database(): print information of the available climate indices (e.g. long_name, url).
get_climate_index(climate_index_name=None): get the climate index as a pandas Series instance (if None, print the database).
plot_climate_index(climate_index_name): plot the climate index time series.
Notebook Examples

http://nbviewer.ipython.org/github/wy2136/climate_index/blob/master/climate_index.ipynb

Documentation

https://dl.dropboxusercontent.com/u/16364556/climate_index_doc/html/index.html
"""

setup(name=DISTNAME,
      version=VERSION,
      license=LICENSE,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      classifiers=CLASSIFIERS,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      install_requires=INSTALL_REQUIRES,
      url=URL,
      packages=find_packages())