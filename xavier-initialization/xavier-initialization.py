import numpy as np
def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    # Write code here
    W = np.asarray(W)
    fan_in = np.asarray(fan_in)
    fan_out = np.asarray(fan_out)
    l = np.sqrt(6 / (fan_in + fan_out))

    W = W * 2 * l - l

    return W