import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)
    n_sample, n_feature = X.shape
    
    w = np.zeros(n_feature)
    b = 0

    for i in range(steps):
        z = np.dot(X, w) + b
        y_pred = _sigmoid(z)

        delta_w = np.dot(X.T, (y_pred - y)) / n_sample
        delta_b = np.sum(y_pred - y) / n_sample

        w = w - lr * delta_w
        b = b - lr * delta_b
    return (w, b)
    pass