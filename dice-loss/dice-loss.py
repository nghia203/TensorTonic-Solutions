import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    # Write code here
    p = np.asarray(p).flatten()
    y = np.asarray(y).flatten()
    dice = (2*np.sum(p*y)+eps)/(np.sum(p+y)+eps)
    loss = 1 - dice
    return loss
    pass