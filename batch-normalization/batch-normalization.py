import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x = np.asarray(x)
    gamma = np.asarray(gamma)
    beta = np.asarray(beta)
    
    ndim = x.ndim

    if ndim == 2:
        axes = 0
    elif ndim == 4:
        axes = (0, 2, 3)

    mean = np.mean(x, axis = axes, keepdims = True)
    var = np.var(x, axis = axes, keepdims = True)

    x_hat = (x - mean) / np.sqrt(var + eps)

    if ndim == 4:
        gamma = gamma.reshape(1, -1, 1, 1)
        beta = beta.reshape(1, -1, 1, 1)

    out = gamma * x_hat + beta

    return out
    pass