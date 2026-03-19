import numpy as np

def cross_entropy_loss(y_true, y_pred, eps = 1e-15):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    batch_size = y_pred.shape[0]
    y_pred = np.clip(y_pred, eps, 1 - eps)

    conf = y_pred[np.arange(batch_size), y_true]
    loss = np.log(conf)

    return -np.mean(loss)
    pass