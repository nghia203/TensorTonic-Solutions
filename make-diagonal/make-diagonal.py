import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here

    n = len(v)
    d = np.zeros((n, n))
    for i in range(0, n):
        if v[i] != 0:
            d[i][i] = v[i]
    return d
    pass
