import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)
    return np.mean(np.where(np.abs(y_true - y_pred) > delta, delta * (np.abs(y_true - y_pred) - 0.5 * delta), 0.5 * np.abs(y_true - y_pred)**2))
    pass