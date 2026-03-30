import numpy as np

def nesterov_momentum_step(w, v, grad, lr=0.01, momentum=0.9):
    """
    Perform one Nesterov Momentum update step.
    """
    # Write code here
    w = np.asarray(w, dtype = np.float64)
    v = np.asarray(v, dtype = np.float64)
    grad = np.asarray(grad, dtype = np.float64)

    v = momentum * v + lr * grad

    w -= v

    return w, v
    pass