from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import root_mean_squared_error
import pandas as pd


def get_r2_rmse(file_name, Y):
    data = pd.read_csv(file_name, index_col=0)
    features = data.drop(Y, axis=1)
    target = data[Y]
    features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.25, random_state=42)
    model = LinearRegression()
    model.fit(features_train, target_train)
    result = model.predict(features_test)
    rmse = root_mean_squared_error(target_test, model)
    r2 = r2_score(target_test, result)
    return [r2, rmse]