import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    counts = Counter(x)
    return np.mean(x), np.median(x), counts.most_common(1)[0][0]
    pass