import numpy as np

def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here
    median = []
    for i in range(len(values) - window_size + 1):
        window = values[i : i + window_size]
        median.append(np.median(window))
    return median