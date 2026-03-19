import numpy as np

class VanillaRNN:
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        self.hidden_dim = hidden_dim

        # Xavier initialization
        self.W_xh = np.random.randn(hidden_dim, input_dim) * np.sqrt(2.0 / (input_dim + hidden_dim))
        self.W_hh = np.random.randn(hidden_dim, hidden_dim) * np.sqrt(2.0 / (2 * hidden_dim))
        self.W_hy = np.random.randn(output_dim, hidden_dim) * np.sqrt(2.0 / (hidden_dim + output_dim))
        self.b_h = np.zeros(hidden_dim).reshape(-1, 1)
        self.b_y = np.zeros(output_dim)

    def forward(self, X: np.ndarray, h_0: np.ndarray = None) -> tuple:
        """
        Forward pass through entire sequence.
        Returns (y_seq, h_final).
        """
        # YOUR CODE HERE
        batch_size, seq_len, _ = X.shape
    
        h_0 = np.zeros((batch_size, self.hidden_dim))

        h_prev = h_0

        y_list = []

        for t in range(seq_len):
            x_t = X[:, t, :]

            w1 = np.dot(self.W_xh, x_t.T)
            w2 = np.dot(self.W_hh, h_prev.T)
            h_t = np.tanh(w1 + w2 + self.b_h).T

            y_t = (np.dot(self.W_hy, h_t.T) + self.b_y).T

            y_list.append(y_t)

            h_prev = h_t

        y_seq = np.stack(y_list, axis = 1)

        return y_seq, h_prev
                        
        
        pass