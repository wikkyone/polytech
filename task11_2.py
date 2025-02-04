from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LinearRegression


def fit_and_predict(features_train, features_test, target_train, target_test):
    model = LinearRegression()
    model.fit(features_train, target_train)
    result = model.predict(features_test)
    return result