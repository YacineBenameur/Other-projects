
from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=50, random_state=0)

               

class Regressor(BaseEstimator):
    def fit(self, X, y):
        self.reg = RandomForestRegressor(n_estimators=50, random_state=0)
        self.reg.fit(X, y)

    def predict(self, X):
        return self.reg.predict(X)
