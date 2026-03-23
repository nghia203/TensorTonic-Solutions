import numpy as np

def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code here
    X = np.asarray(X)
    W = np.asarray(W)
    b = np.asarray(b)
    num_samples, _ = X.shape

    _, d_out = W.shape

    y = np.zeros((num_samples, d_out))

    y = np.dot(X, W) + b
    return y.tolist()
    