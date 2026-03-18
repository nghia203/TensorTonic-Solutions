import numpy as np
def rolling_std(values, window_size):
    """
    Compute the rolling population standard deviation.
    """
    # Write code here
    values = np.asarray(values)
    window = []

    rsd = []
    for i in range(0, len(values) - window_size + 1):
        window = values[i : i + window_size]

        mean = np.mean(window)

        std = np.sqrt(np.sum((window - mean)**2) / len(window))

        rsd.append(std)

    return rsd