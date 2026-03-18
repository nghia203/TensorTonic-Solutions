import numpy as np

def softmax(x, axis=-1):
    e_x = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e_x / np.sum(e_x, axis=axis, keepdims=True)

def multi_head_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray,
                         W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray,
                         W_o: np.ndarray, num_heads: int) -> np.ndarray:
    """
    Compute multi-head attention.
    """
    # Your code here
    batch_size, seq_len, d_model = Q.shape
    d_k = d_model // num_heads
    Q = np.dot(Q, W_q)
    K = np.dot(K, W_k)
    V = np.dot(V, W_v)

    def split_heads(X):
        X = X.reshape(batch_size, seq_len, num_heads, d_k)
        return X.transpose(0, 2, 1, 3)

    Q = split_heads(Q)
    K = split_heads(K)
    V = split_heads(V)

    K_t = K.transpose(0, 1, 3, 2)

    scores = np.matmul(Q, K_t) / np.sqrt(d_k)

    weights = softmax(scores, axis = -1)

    context = np.matmul(weights, V)

    context = context.transpose(0, 2, 1, 3).reshape(batch_size, seq_len, d_model)
    return np.dot(context, W_o)
    return np.matmul(concat, W_o)
    pass