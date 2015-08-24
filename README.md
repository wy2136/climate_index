# climate_index
Download and visulize climate indices from NOAA website: http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/

Major APIs:
* print_database(): print information of the available climate indices (e.g. long_name, url).
* get_climate_index(climate_index_name=None): get the climate index as a pandas Series instance (if None, print the database).
* plot_climate_index(climate_index_name): plot the climate index time series.

Notebook Introduction: http://nbviewer.ipython.org/urls/dl.dropbox.com/s/m6cvln2it3w5rcz/climate_index.ipynb
