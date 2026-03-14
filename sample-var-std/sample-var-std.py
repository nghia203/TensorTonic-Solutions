import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    mean = np.mean(x)
    deviation = (mean - x)**2
    var = np.sum(deviation) / (len(x) - 1)
    return var, np.sqrt(var)
    pass