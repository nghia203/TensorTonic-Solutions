import numpy as np
from scipy.special import factorial
def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    pmf = np.exp(-lam) * lam**k / factorial(k)
    cdf = [np.exp(-lam) * lam**i / factorial(i) for i in range(0, k+1)]
    return pmf, np.sum(cdf)
    pass