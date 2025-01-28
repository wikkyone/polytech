import pandas as pd
import numpy as np

def get_variation(file_name):
    data = pd.read_csv(file_name)
    std = np.std(data['Male Life Expectancy'])
    mean = np.mean(data['Male Life Expectancy'])
    var = std/mean * 100
    return round(var,2)