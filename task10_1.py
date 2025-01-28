import pandas as pd
import numpy as np

def get_statistics(int_list):
    mean = np.mean(int_list)
    median = np.median(int_list)
    return [mean, median]