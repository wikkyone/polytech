import pandas as pd


def max_min_column(df, clmn):
    col_max = df[clmn].max()
    col_min = df[clmn].min()
    return f"Max = {col_max}, min = {col_min}"
