import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    ret=0.0
    n= len(x)
    check=0.0
    for i in range(n):
        check+=p[i]

    if check!=1:
            raise ValueError()
    for i in range(n):
        ret= ret+ (x[i]*p[i])


    return ret