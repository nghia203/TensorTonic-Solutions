import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    if len(x) != len(y):
        raise ValueError
    x = np.asarray(x)
    y = np.asarray(y)

    return sum(x * y)
    pass