# Climate Index
Download and visulize climate indices from NOAA website
http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/

## Major APIs:
* `print_database()`: print information of the available climate indices (e.g. long_name, url).
* `get_climate_index(climate_index_name=None)`: get the climate index as a pandas Series instance (if None, print the database).
* `plot_climate_index(climate_index_name)`: plot the climate index time series.

## Notebook Examples
http://nbviewer.ipython.org/github/wy2136/climate_index/blob/master/climate_index.ipynb

## Documentation
https://dl.dropboxusercontent.com/u/16364556/climate_index_doc/html/index.html
