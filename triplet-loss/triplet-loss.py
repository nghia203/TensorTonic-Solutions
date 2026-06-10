import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    # Write code here
    anchor = np.asarray(anchor)
    positive = np.asarray(positive)
    negative = np.asarray(negative)
    axis = 1 if anchor.ndim > 1 else 0
    d1 = np.linalg.norm(anchor - positive, axis=axis)**2

    d2 = np.linalg.norm(anchor - negative, axis=axis)**2

    loss = np.maximum(0, d1 - d2 + margin)
    return np.mean(loss)
    pass