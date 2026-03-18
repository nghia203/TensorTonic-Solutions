import numpy as np

def softmax(x, axis=-1):
    """Provided: Softmax function."""
    e_x = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e_x / np.sum(e_x, axis=axis, keepdims=True)

def layer_norm(x: np.ndarray, gamma: np.ndarray, beta: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    """
    Apply layer normalization.
    """
    # Your code here
    mean = np.mean(x, axis = -1, keepdims = True)
    var = np.var(x, axis = -1, keepdims = True)

    norm = gamma * (x - mean) / (np.sqrt(var) + eps) + beta
    return norm
    pass

def multi_head_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray,
                         W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray,
                         W_o: np.ndarray, num_heads: int) -> np.ndarray:
    """
    Multi-head attention.
    """
    # Your code here
    batch_size, seq_len, d_model = Q.shape
    d_k = d_model // num_heads

    Q = np.dot(Q, W_q)
    K = np.dot(K, W_k)
    V = np.dot(V, W_v)

    def split_heads(x):
        x = x.reshape(batch_size, seq_len, num_heads, d_k)
        return x.transpose(0, 2, 1, 3)

    Q = split_heads(Q)
    K = split_heads(K)
    V = split_heads(V)

    K_t = K.transpose(0, 1, 3, 2)
    
    scores = np.matmul(Q, K_t) / np.sqrt(d_k)

    weight = softmax(scores, axis = -1)

    context = np.matmul(weight, V)

    context = context.transpose(0, 2, 1, 3).reshape(batch_size, seq_len, d_model)

    return np.dot(context, W_o)
    pass

def feed_forward(x: np.ndarray, W1: np.ndarray, b1: np.ndarray,
                 W2: np.ndarray, b2: np.ndarray) -> np.ndarray:
    """
    Position-wise feed-forward network.
    """
    # Your code here
    h = np.dot(x, W1) + b1

    h_a = np.maximum(0, h)

    return np.dot(h_a, W2) + b2
    pass

def encoder_block(x: np.ndarray, W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray,
                  W_o: np.ndarray, W1: np.ndarray, b1: np.ndarray, W2: np.ndarray,
                  b2: np.ndarray, gamma1: np.ndarray, beta1: np.ndarray,
                  gamma2: np.ndarray, beta2: np.ndarray, num_heads: int) -> np.ndarray:
    """
    Complete encoder block: MHA + FFN with residuals and layer norms.
    """
    # Your code here
    att_output = multi_head_attention(x, x, x, W_q, W_k, W_v, W_o, num_heads)
    x_a = layer_norm(x + att_output, gamma1, beta1)
    feed_output = feed_forward(x_a, W1, b1, W2, b2)
    return layer_norm(x_a + feed_output, gamma2, beta2)
    pass