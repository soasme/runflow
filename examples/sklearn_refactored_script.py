# File: examples/sklearn_refactored_script.py
from sklearn.datasets import load_boston
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
import pandas as pd

class ExtractTrainingSet:

    def run(self):
        df = load_boston()
        return dict(
            x=pd.DataFrame(df.data, columns=df.feature_names),
            y=pd.DataFrame(df.target, columns=['target'])
        )

class TrainModel:

    MODELS = {
        'ols': LinearRegression,
        'gbm': GradientBoostingRegressor,
    }

    def __init__(self, model, x, y):
        if model not in self.MODELS:
            raise ValueError(f'invalid model: {model}')
        self.model = model
        self.x = x
        self.y = y

    def run(self):
        model = self.MODELS[self.model]()
        model.fit(self.x, self.y)
        score = model.score(self.x, self.y)
        return {'score': score}
