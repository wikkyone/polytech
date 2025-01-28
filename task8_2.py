import pandas as pd


def series_index(data, indexes):
    series = pd.Series(data, index=indexes)
    return series


print(series_index(data=[21, 23, 5], indexes=["июль", "июнь", "август"]))
