from sklearn.datasets import load_boston
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
import pandas as pd

# extract test set
df = load_boston()
df_trainX = pd.DataFrame(df.data, columns=df.feature_names)
df_trainY = pd.DataFrame(df.target, columns=['target'])

# train ols model
model1 = LinearRegression()
model1.fit(df_trainX, df_trainY)
score1 = model1.score(df_trainX, df_trainY)

# train gbm
model2 = GradientBoostingRegressor()
model2.fit(df_trainX, df_trainY)
score2 = model2.score(df_trainX, df_trainY)

# report the better model
if score1 > score2:
    print("choose ols model")
elif score1 < score2:
    print("choose gbm model")
else:
    print("gbm/ols model are both okay")
