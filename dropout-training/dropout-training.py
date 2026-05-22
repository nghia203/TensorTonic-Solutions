import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.asarray(x)
    if rng:
        rand_matrix = rng.random(size=x.shape) 
    else:
        rand_matrix = np.random.random(size=x.shape)

    dropout_pattern = (rand_matrix >= p).astype(float) / (1.0 - p)

    return dropout_pattern * x, dropout_pattern
    pass