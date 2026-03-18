import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    C = np.asarray(C)
    row = np.sum(C, axis = 1)
    col = np.sum(C, axis = 0)

    expected = np.outer(row, col) / np.sum(C)

    return np.sum((C - expected)**2 / expected), expected
    pass