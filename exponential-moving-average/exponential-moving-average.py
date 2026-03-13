import numpy as np
def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    # Write code here
    ema = [values[0]]
    values_array = np.asarray(values)
    for i in range(1, len(values_array)):
        ema.append(alpha * values_array[i] + (1 - alpha) * ema[i - 1])
    return ema