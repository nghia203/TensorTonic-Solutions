import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x_sort = np.sort(x)
    p = []
    for i in range(len(q)):
        p.append(np.percentile(x, q[i], method='linear'))
    return np.asarray(p)
    pass