import numpy as np

def confusion_matrix_norm(y_true, y_pred, num_classes=None, normalize='none'):
    """
    Compute confusion matrix with optional normalization.
    """
    # Write code here

    y_pred = np.asarray(y_pred, dtype = np.int64)
    y_true = np.asarray(y_true, dtype = np.int64)

    if y_true.size == 0:
        K = num_classes if num_classes is not None else 0
        return np.zeros((K, K), dtype=np.int64 if normalize == 'none' else np.float64)

    K = num_classes if num_classes is not None else int(np.max([y_true, y_pred]) + 1)
    
    indices = y_true * K + y_pred
    cm = np.bincount(indices, minlength = K * K).reshape(K, K)
    
    if normalize == 'none':
        return cm.astype(np.int64)

    cm = cm.astype(np.float64)
    epsilon = 1e-15
    
    if normalize == 'true':
        cm /= (cm.sum(axis = 1, keepdims = True) + epsilon)
    elif normalize == 'pred':
        cm /= (cm.sum(axis = 0, keepdims = True) + epsilon)
    elif normalize == 'all':
        cm /= (cm.sum() + epsilon)
    return cm
    pass