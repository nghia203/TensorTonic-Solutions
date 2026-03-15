import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X)
    if len(X) < 2 or X.ndim != 2:
        return None
    mean = np.mean(X, axis = 0)
    centered = X - mean
    cov = (centered.T @ centered) / (len(X) - 1)
    return cov
    pass