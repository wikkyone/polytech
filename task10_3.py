import numpy as np

def get_stats(size, mode):
    arr = np.random.choice([mode, mode + 100, mode - 100], size, p=[0.5, 0.25, 0.25])
    median = np.median(arr)
    average = np.mean(arr)
    std = np.std(arr)
    return arr,[median, average, std]