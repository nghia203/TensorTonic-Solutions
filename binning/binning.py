import numpy as np
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    v_max = max(values)
    v_min = min(values)
    if v_min == v_max:
        return np.zeros(len(values), dtype=int).tolist()
    values = np.asarray(values)
    bin = (v_max - v_min) / num_bins
    clamp = np.minimum(np.floor((values - v_min) / bin), num_bins - 1)
    return clamp.tolist()