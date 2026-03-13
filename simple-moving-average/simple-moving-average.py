import numpy as np

def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    values = np.asarray(values)
    
    weights = np.ones(window_size) / window_size
    
    sma = np.convolve(values, weights, mode='valid')
    
    return sma.tolist()