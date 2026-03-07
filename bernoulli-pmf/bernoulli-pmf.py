import numpy as np
import time

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    x = np.asarray(x)
    start = time.time()
    pmf = np.where(x == 1, p, 1 - p)
    
    duration = time.time() - start

    mean = float(p)
    var = float(p * (1 - p))
    
    return pmf, mean, var
    pass