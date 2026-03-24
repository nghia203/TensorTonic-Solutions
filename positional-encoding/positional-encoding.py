import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pe = np.zeros((seq_len, d_model))

    pos = np.arange(seq_len)[:, np.newaxis]

    div_term = np.exp(np.arange(0, d_model, 2) * -(np.log(base) / d_model))

    pe[:, 0::2] = np.sin(pos * div_term)

    if d_model > 1:
        pe[:, 1::2] = np.cos(pos * div_term[:d_model // 2])

    return pe
    pass