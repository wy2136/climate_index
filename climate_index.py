# 
# Download and plot climate indices from the NOAA website.
# 
# Written by Wenchang Yang (yang.wenchang@uci.edu)
# 

from __future__ import print_function
import pandas as pd

database = {
    'soi': {
        'long_name': 'Southern Oscillation Index',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/soi.long.data',
        'invalid_value': -10.0,
    },
    'nao': {
        'long_name': 'North Atlantic Oscillation',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/nao.long.data',
        'invalid_value': -99.99,
    },
    'rnao': {
        'long_name': 'Reconstructed monthly NAO index back to December 1658',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/rnao.long.data',
        'invalid_value': -99.90,
    },
    'ao':{
        'long_name': 'Arctic Oscillation Index',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/ao.long.data',
        'invalid_value': -9.990,
    },
    'ao20r': {
        'long_name': 'Arctic Oscillation Index from the 20thC Reanalysis',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/ao20thc.long.data',
        'invalid_value': -999.0,
    },
    'pdo': {
        'long_name': 'Pacific Decadal Oscillation',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/pdo.long.data',
        'invalid_value': -9.90,
    },
    'np': {
        'long_name': 'North Pacific Index',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/np.long.data',
        'invalid_value': -999.0,
    },
    'tp': {
        'long_name': 'Trans Polar Index',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/tpi.long.data',
        'invalid_value': -9.99,
    },
    'ip': {
        'long_name': 'Iceland SLP',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/nao_ice.long.data',
        'invalid_value': -10,
    },
    'ap': {
        'long_name': 'Ponta Delgada, Azores SLP',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/nao_azo.long.data',
        'invalid_value': -10,
    },
    'gp': {
        'long_name': 'Gibraltar SLP',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/nao_gib.long.data',
        'invalid_value': -10,
    },
    'nslp': {
        'long_name': 'Nagasaki SLP',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/nagasakipres.long.data',
        'invalid_value': -10,
    },
    'mp': {
        'long_name': 'Madras SLP',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/madrasslp.long.data',
        'invalid_value': -10,
    },
    'nino12': {
        'long_name': 'Nino 1+2 SST Index',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/nino12.long.anom.data',
        'invalid_value': -99.99,
    },
    'nino3': {
        'long_name': 'Nino 3 SST Index',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/nino3.long.anom.data',
        'invalid_value': -99.99,
    },
    'nino34': {
        'long_name': 'Nino 3.4 SST Index',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/nino34.long.anom.data',
        'invalid_value': -99.99,
    },
    'nino4': {
        'long_name': 'Nino 4 SST Index',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/nino4.long.anom.data',
        'invalid_value': -99.99,
    },
    'amo': {
        'long_name': 'Atlantic multidecadal oscillation SST Index',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/amo.long.data',
        'invalid_value': -99.99,
    },
    'amo_sm': {
        'long_name': 'Atlantic multidecadal oscillation SST Index (smoothed)',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/amo.sm.long.data',
        'invalid_value': -99.990,
    },
    'amo_detrend': {
        'long_name': 'Atlantic multidecadal oscillation SST Index (detrended)',
        'url': 'http://www.esrl.noaa.gov/psd/data/correlation//amon.us.long.data',
        'invalid_value': -99.99,
    },
    'amo_detrend_sm': {
        'long_name': 'Atlantic multidecadal oscillation SST Index (detrended, smoothed)',
        'url': 'http://www.esrl.noaa.gov/psd/data/correlation/amon.sm.long.data',
        'invalid_value': -99.990,
    },
    'global_t_station': {
        'long_name': 'Global Average Temperature Anomalies (Station Only)',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/GLBTS.long.data',
        'invalid_value': -999,
    },
    'global_t_sst': {
        'long_name': 'Global Average Temperature & SST Anomalies (Station + SST)',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/GLBTSSST.long.data',
        'invalid_value': -999,
    },
    'global_t_cru': {
        'long_name': 'Global Average Temperature Anomaly (CRU)',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/taveglhc4.long.data',
        'invalid_value': -99.99,
    },
    'sunspot': {
        'long_name': 'Sunspot Index',
        'url': 'http://www.esrl.noaa.gov/psd/gcos_wgsp/Timeseries/Data/sunspot.long.data',
        'invalid_value': -99.9,
    },
}
def print_database():
    for name in sorted(database.keys()):
        print(name.upper())
        print(' '*4, database[name]['long_name'])
        print(' '*4, database[name]['url'])
def _get_year_start_end(climate_index_name):
    '''Get the start and end years as a tuple.'''
    url = database[climate_index_name.lower()]['url']
    df = pd.read_csv(url, header=None, nrows=1, sep=r'\s+')
    year_start = df.iloc[0,0]
    year_end = df.iloc[0,1]
    return year_start, year_end
# year_start, year_end = _get_year_start_end('nino34')
def _get_number_of_years(year_start, year_end):
    return len(range(year_start, year_end)) + 1
def _read_csv(climate_index_name):
    url = database[climate_index_name.lower()]['url']
    year_start, year_end = _get_year_start_end(climate_index_name)
    Nyears = _get_number_of_years(year_start, year_end)
    if year_start < 1678:# ignore records before 1678 since pandas is not able to handle this
        Nskiprecords = 1678 - year_start
    else:
        Nskiprecords = 0
    df = pd.read_csv(url, header=None, skiprows=1+Nskiprecords, 
        nrows=Nyears-Nskiprecords, 
        sep=r'\s+', index_col=0, 
        na_values=database[climate_index_name.lower()]['invalid_value'])
    return df
# df = read_csv('nino34')
def _get_year_month_index(year_start, year_end):
    if year_start < 1678: # pandas is not able to handle date before 1678
        year_start = 1678
    Nyears = _get_number_of_years(year_start, year_end)
    year_month_index = pd.date_range(
        str(year_start)+'-01', periods=Nyears*12, freq='M'
    ).to_period()
    return year_month_index
# year_month_index = _get_year_month_index(1870, 2015)
def get_climate_index(climate_index_name=None):
    if climate_index_name is None:
        print_database()
        return
    year_start, year_end = _get_year_start_end(climate_index_name)
    year_month_index = _get_year_month_index(year_start, year_end)
    df = _read_csv(climate_index_name).iloc[:,0:12]
    climate_index = pd.Series(df.values.ravel(), 
        index=year_month_index, name=climate_index_name.upper())
    return climate_index
def plot_climate_index(climate_index_name):
    climate_index = get_climate_index(climate_index_name)
    climate_index.plot()
    plt.legend()
# plot_climate_index('nino34')
# plot_climate_index('nino12')
# plot_climate_index('pdo')