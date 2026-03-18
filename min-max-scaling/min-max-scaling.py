import numpy as np

def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    data = np.asarray(data)
    
    max = np.max(data, axis = 0, keepdims = True)
    min = np.min(data, axis = 0, keepdims = True)

    det = np.maximum(max - min, 1e-9)

    data_scaled = (data - min) / det
    return data_scaled.tolist()