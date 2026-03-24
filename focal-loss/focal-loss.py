import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    p=np.array(p)
    y=np.array(y)
    # Write code here
    one = -((1-p)**gamma)*y*np.log(p)
    two = (p**gamma)*(1-y)*(np.log(1-p))
    three = one - two 
    return np.mean(three) 