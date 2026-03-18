import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here

    x = np.asarray(x)
    mean = np.mean(x, axis = -1)
    
    s = np.sqrt(np.sum((x - mean)**2) / (len(x) - 1))
    t = (mean - mu0) / (s / np.sqrt(len(x)))
    return t
    pass