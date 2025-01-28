import pandas as pd

def get_mode(int_list):
    data = pd.Series(int_list)
    mode = data.mode()[0]
    return mode