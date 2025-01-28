import pandas as pd


def val_counts(data, clmn):
    return data[clmn].value_counts(normalize=True)
