import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X)
    if len(X) < 2 or X.ndim != 2:
        return None
    std = np.std(X, axis = 0, ddof = 1)
    std_safe = std.copy()
    zero_variance_mask = (std_safe == 0)
    std_safe[zero_variance_mask] = 1.0
    
    cor = np.cov(X, rowvar = False) / np.outer(std, std)

    if np.any(zero_variance_mask):
        cor[zero_variance_mask, :] = np.nan
        cor[:, zero_variance_mask] = np.nan
    return cor
    pass