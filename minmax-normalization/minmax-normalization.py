import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    col_min = np.min(X, axis = axis, keepdims = True)
    col_max = np.max(X, axis = axis, keepdims = True)
    det = np.maximum(col_max - col_min, eps)

    x_t = (X - col_min) / det
    return x_t 
    pass