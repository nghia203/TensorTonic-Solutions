import numpy as np

def _entropy(y):
    """
    Helper: Compute Shannon entropy (base 2) for labels y.
    """
    y = np.asarray(y)
    if y.size == 0:
        return 0.0
    vals, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) if p.size else 0.0

def information_gain(y, split_mask):
    """
    Compute Information Gain of a binary split on labels y.
    Use the _entropy() helper above.
    """
    # Write code here
    y = np.asarray(y)
    n_parent = y.size
    
    e_y = _entropy(y)

    y_left = y[split_mask]
    y_right = y[~split_mask]

    n_left = y_left.size
    n_right = y_right.size

    if n_left == 0 or n_right == 0:
        return 0

    e_left = _entropy(y_left)
    e_right = _entropy(y_right)

    e_child = n_left / n_parent * e_left + n_right / n_parent * e_right

    ig = e_y - e_child

    return ig
    pass
