import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.asarray(x)
    x_max = np.max(x, axis = -1, keepdims = True)
    exp_cal = np.exp(x - x_max)
    exp_sum = np.sum(exp_cal, axis = -1, keepdims = True)
    sm = exp_cal / exp_sum
    return sm
    pass