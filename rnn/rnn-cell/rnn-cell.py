import numpy as np

def rnn_cell(x_t: np.ndarray, h_prev: np.ndarray, 
             W_xh: np.ndarray, W_hh: np.ndarray, b_h: np.ndarray) -> np.ndarray:
    """
    Single RNN cell forward pass.
    """
    # YOUR CODE HERE
    b_h = b_h.reshape(-1, 1)
    w1 = np.dot(W_hh, h_prev.T)
    w2 = np.dot(W_xh, x_t.T)
    h = np.tanh(w1 + w2 + b_h)
    return h.T
    pass