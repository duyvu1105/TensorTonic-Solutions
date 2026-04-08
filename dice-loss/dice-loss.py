import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    # Write code here
    p = np.asarray(p).flatten()
    y = np.asarray(y).flatten()
    dice = (np.dot(p, y) * 2 + eps) / (np.sum(p) + np.sum(y) + eps)
    return 1 - dice