import numpy as np

def compute_gradient_norm_decay(T: int, W_hh: np.ndarray) -> list:
    """
    Simulate gradient norm decay over T time steps.
    Returns list of gradient norms.
    """
    # YOUR CODE HERE
    grad = 1.0
    grad_list = [(grad)]
    for t in range(1, T):
        norm = np.linalg.norm(W_hh, ord = 2)
        grad = grad * norm
        grad_list.append(grad)
    return grad_list
    pass