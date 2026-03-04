import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x=np.array(x)
    gamma=np.array(gamma)
    beta= np.array(beta)
    
    if x.ndim ==2:
        total_length=x.shape[0]
        mio = np.mean(x,axis=0,keepdims=True)

        sigma = np.var(x,axis=0,keepdims=True)

        xnew=np.zeros_like(x)
        ynew=np.zeros_like(x)
        xnew = (x-mio) /np.sqrt(sigma+eps)

        ynew = gamma*xnew+beta 

    elif x.ndim == 4:
        total_length=x.shape[0]

        mio= np.mean(x,axis=(0,2,3),keepdims=True)

        sigma = np.var(x,axis= (0,2,3),keepdims=True)
        xnew=np.zeros_like(x)
        ynew=np.zeros_like(x)

        xnew=(x-mio)/np.sqrt(sigma+eps)

        C=x.shape[1]
        gamma=gamma.reshape(1,C,1,1)
        beta=beta.reshape(1,C,1,1)
        ynew=gamma*xnew+beta

    return ynew