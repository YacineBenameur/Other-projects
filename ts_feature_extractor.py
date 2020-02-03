import sys
!conda install --yes --prefix {sys.prefix} holidays

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
        df = X_ds.to_dataframe()
        df['time'] = pd.to_datetime(X_ds['time'])
        df = df.iloc[X_ds.n_burn_in:,:]
        
        df['year'] = [d.year for d in df['time']]
        df['month'] = [d.month for d in df['time']]
        df['day_of_week'] = [d.weekday() for d in df['time']]
        df['day_of_month'] = [d.day for d in df['time']]
        
        # dummy variable for holiday

        GH = holidays.France()

        df['holiday'] = 0

        for date in df.index:
            if date in GH:
                df.loc[date,'holiday'] = 1


        
        return df[['year','day_of_week','month','day_of_month','holiday']].values