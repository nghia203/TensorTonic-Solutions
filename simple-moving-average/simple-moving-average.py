import numpy as np
def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here
    sma = []
    values = np.asarray(values)
    for i in range(len(values) - window_size + 1):
        window = values[i : i + window_size]
        sma.append(np.sum(window) / window_size)
    return sma