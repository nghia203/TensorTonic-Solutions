import numpy as np

def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    
    cos = np.dot(x1, x2) / (np.linalg.norm(x1) * np.linalg.norm(x2))

    if label == 1:
        return 1 - cos
    elif label == -1:
        return np.maximum(0, cos - margin)
    