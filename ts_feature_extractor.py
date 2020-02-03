import numpy as np
import pandas as pd
import holidays
from sklearn.preprocessing import PolynomialFeatures

class FeatureExtractor(object):

    def __init__(self):
        pass

    def fit (self, X_ds, y_array):
        pass

    def transform(self, X_ds):
        """
        
        """
        df = X_ds.to_dataframe()
        df['time'] = pd.to_datetime(X_ds['time'].values)
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


        X_df = pd.get_dummies(df[['day_of_week','month','day_of_month','holiday']].applymap(str))
        X_df['year'] = df['year'] #year variable is not treated as a categorical variable, so it's not one-hot encoded

        poly_transformer = PolynomialFeatures(degree=2, interaction_only=False,include_bias=True).fit(X_df.values)
        
        X_train = poly_transformer.transform(X_df.values)


        
        return X_train
