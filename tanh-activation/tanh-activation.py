import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x=np.array(x)
    print(type(x))
    # Write code here
    one = np.exp(x)-np.exp(-x)
    two= np.exp(x)+np.exp(-x)
    return one/two