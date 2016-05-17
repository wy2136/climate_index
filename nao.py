#
# NAO daily index from http://www.esrl.noaa.gov/psd/data/timeseries/daily/NAO/.
#
# Written by Wenchang Yang (yang.wenchang@uci.edu)
#
import numpy as np
import pandas as pd
import xarray as xr
import datetime
import os

def get_daily_nao(months=None, years=None, reload_data=False):
    ''' NAO daily index from:
        http://www.esrl.noaa.gov/psd/data/timeseries/daily/NAO/.
        '''
    module_dir, fname = os.path.split(__file__)
    data_file = os.path.join(module_dir, 'data',
        'nao.reanalysis.t10trunc.1948-present.txt')
    data_file_exists = os.path.exists(data_file)
    col_names = ['year', 'month', 'day', 'NAO']
    # read data file
    if data_file_exists and not reload_data:
        # load data from local drive
        df = pd.read_csv(data_file,
            skiprows=0, names=col_names, sep=r'\s+')
    else:
        # download data from the internet
        df = pd.read_csv(
            'ftp://ftp.cdc.noaa.gov/Public/gbates/teleconn/nao.reanalysis.t10trunc.1948-present.txt',
            skiprows=0, names=col_names, sep=r'\s+')

    years_, months_, days_ = (df.loc[:, 'year'], df.loc[:, 'month'],
        df.loc[:,'day'])
    time = [datetime.datetime(year, month, day, 12, 0, 0)
        for year, month, day in zip(years_, months_, days_)]
    df.index = time

    # select columns
    df = df.loc[:, ['NAO']]

    # mask invalid Value
    # df[df>=999] = np.nan

    # convert to xarray Dataset with dimension name "time"
    ds = xr.Dataset.from_dataframe(df)
    ds = ds.rename({'index': 'time'})

    # select months
    if months is not None:
        L = False
        for month in months:
            L = L | (ds['time.month'] == month)
        ds = ds.sel(time=ds['time'][L])
    # select years
    if years is not None:
        L = False
        for year in years:
            L = L | (ds['time.year'] == year)
        ds = ds.sel(time=ds['time'][L])

    return ds['NAO']
