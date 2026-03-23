import numpy as np

def conv2d(x, W, b):
    """
    Simple 2D convolution layer forward pass.
    Valid padding, stride=1.
    """
    # Write code here
    N, C_in, h_x, w_x = x.shape
    C_out, _, h_w, w_w = W.shape

    h_out = h_x - h_w + 1
    w_out = w_x - w_w + 1

    y = np.zeros((N, C_out, h_out, w_out))

    for i in range(N):
        for j in range(C_out):
            for k in range(h_out):
                for l in range(w_out):
                    window = x[i, :, k : k + h_w, l : l + w_w]
                    y[i, j, k, l] = np.sum(window * W[j]) + b[j]
    return y
    pass