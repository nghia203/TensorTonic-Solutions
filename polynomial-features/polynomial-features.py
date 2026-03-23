import numpy as np
def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    values = np.asarray(values)
    result = np.zeros((len(values), degree + 1))

    for p in range(degree + 1):
        result[:, p] = values ** p

    return result.tolist()