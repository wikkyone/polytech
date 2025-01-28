import pandas as pd


def data_shape(file):
    data = pd.read_csv(file)
    return data.shape
