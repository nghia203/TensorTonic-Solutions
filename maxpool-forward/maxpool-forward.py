import numpy as np
def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    # Write code here
    X = np.asarray(X)
    h, w = X.shape
    h_out = int((h - pool_size) / stride) + 1
    w_out = int((w - pool_size) / stride) + 1

    y = np.zeros((h_out, w_out))

    for i in range(h_out):
        for j in range(w_out):
            i_start = i * stride
            j_start = j * stride
            window = X[i_start : i_start + pool_size, j_start : j_start + pool_size]
            y[i][j] = np.max(window)

    return y.tolist()