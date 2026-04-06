import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    # Write code here
    p=np.asarray(p,dtype=float)
    y=np.asarray(y,dtype=float)

    one = 2*np.sum(p*y)
    two = np.sum(p)+np.sum(y)
    val= (one + eps) /(two+eps)
    ret= 1-val 
    return ret