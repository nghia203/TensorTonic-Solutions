import numpy as np

def rnn_forward(X: np.ndarray, h_0: np.ndarray,
                W_xh: np.ndarray, W_hh: np.ndarray, b_h: np.ndarray) -> tuple:
    """
    Forward pass through entire sequence.
    """
    # YOUR CODE HERE
    batch_size, seq_len, input_dim = X.shape
    b_h = b_h.reshape(-1, 1)
    hidden_state = []
    h_prev = h_0
    for t in range(seq_len):
        x_t = X[:, t, :]

        w1 = np.dot(W_hh, h_prev.T)
        w2 = np.dot(W_xh, x_t.T)
        h_t = np.tanh(w1 + w2 + b_h).T

        hidden_state.append(h_t)

        h_prev = h_t

    hidden_states = np.stack(hidden_state, axis = 1)
    h_final = hidden_state[-1]

    return hidden_states, h_final
    pass