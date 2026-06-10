import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    # Write code here
    Z1 = np.asarray(Z1)
    Z2 = np.asarray(Z2)
    
    S = (Z1 @ Z2.T) / temperature

    S_stable = S - np.max(S, axis=1, keepdims=True)

    pos = np.diag(S_stable)
    exp_sums = np.sum(np.exp(S_stable), axis=1)

    return -np.mean(pos - np.log(exp_sums))
    pass