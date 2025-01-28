import pandas as pd


def row_col_num(f):
    data = pd.read_csv(f)
    shape = data.shape
    return f"В таблице {shape[0]} строк и {shape[1]} столбцов"
