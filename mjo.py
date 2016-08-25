#
# MJO index from http://www.bom.gov.au/climate/mjo/graphics/rmm.74toRealtime.txt.
#
# Written by Wenchang Yang (yang.wenchang@uci.edu)
#
import numpy as np
import pandas as pd
import xarray as xr
import datetime
import os

def get_mjo(months=None, years=None, reload_data=False):
    '''MJO index from
        http://www.bom.gov.au/climate/mjo/graphics/rmm.74toRealtime.txt'''
    module_dir, fname = os.path.split(__file__)
    data_file = os.path.join(module_dir, 'data', 'rmm.74toRealtime.txt')
    data_file_exists = os.path.exists(data_file)
    col_names = ['year', 'month', 'day',
        'RMM1', 'RMM2', 'phase', 'amplitude', 'Missing Value']
    # read data file
    if data_file_exists and not reload_data:
        # load data from local drive
        df = pd.read_csv(data_file,
            skiprows=2, names=col_names, sep=r'\s+')
    else:
        # download data from the internet
        df = pd.read_csv(
            'http://www.bom.gov.au/climate/mjo/graphics/rmm.74toRealtime.txt',
            skiprows=2, names=col_names, sep=r'\s+')

    # time index
    # year0, month0, day0 = df.loc[0, ['year', 'month', 'day']]
    # time = pd.date_range('{}-{}-{} 12:00:00'.format(year0, month0, day0),
    #     periods=len(df), freq='D')
    # df.index = time
    years_, months_, days_ = (df.loc[:, 'year'], df.loc[:, 'month'],
        df.loc[:,'day'])
    # time = []
    # for year, month, day in zip(years, months, days):
    #     time.append(datetime.datetime(year, month, day, 12, 0, 0))
    time = [datetime.datetime(year, month, day, 12, 0, 0)
        for year, month, day in zip(years_, months_, days_)]
    df.index = time

    # select columns
    df = df.loc[:, ['RMM1', 'RMM2', 'phase', 'amplitude']]

    # mask invalid Value
    df[df>=999] = np.nan

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

    return ds
