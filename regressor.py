from sklearn.base import BaseEstimator
from sklearn.linear_model import Ridge
               

class Regressor(BaseEstimator):
    def fit(self, X, y):
        self.reg = Ridge(alpha=1)
        self.reg.fit(X, y)

    def predict(self, X):
        return self.reg.predict(X)
