import numpy as np
import pandas as pd
import holidays


class FeatureExtractor(object):

    def __init__(self):
        pass

    def fit (self, X_ds, y_array):
        pass

    def transform(self, X_ds):
        """
        
        """
        # This is the range for which features should be provided. Strip
        # the burn-in from the beginning.
        valid_range = np.arange(X_ds.n_burn_in, len(X_ds['time']))
        X_df = X_ds.to_dataframe()
        weekly_rolling_mean = X_df.rolling(7).mean().values[valid_range]
        yearly_rolling_mean = X_df.rolling(356).mean().values[valid_range]
        yesterday = np.roll(X_df.values, 1, axis=0)[valid_range]
        week_ago = np.roll(X_df.values, 6, axis=0)[valid_range]
        month_ago = np.roll(X_df.values, 30, axis=0)[valid_range]
        month_ago_2 = np.roll(X_df.values, 31, axis=0)[valid_range]
        week_ago_2 = np.roll(X_df.values, 7, axis=0)[valid_range]
        year_ago = np.roll(X_df.values, 7 * 52 - 1, axis=0)[valid_range]
        day_of_week = np.tile(X_df.index.dayofweek.values, (X_df.shape[1], 1)).T[valid_range]
        store_id = np.tile(np.arange(X_df.shape[1]), (valid_range.shape[0], 1))
        
        df = X_ds.to_dataframe()
        df['time'] = pd.to_datetime(X_ds['time'].values)
        df['day_of_month'] = [d.day for d in df['time']]
        df['month'] = [d.month for d in df['time']]
        
        GH = holidays.France()

        df['holiday'] = 0

        for date in df.index:
            if date in GH:
                df.loc[date,'holiday'] = 1
                
        return np.hstack([
            year_ago,
            week_ago,
            week_ago_2,
            month_ago,
            month_ago_2,
            yesterday,
            weekly_rolling_mean,
            yearly_rolling_mean,
            day_of_week,
            store_id,
            df['holiday'].values[valid_range].reshape((-1,1)),
            df['day_of_month'].values[valid_range].reshape((-1,1)),
            df['month'].values[valid_range].reshape((-1,1)),
        ])
