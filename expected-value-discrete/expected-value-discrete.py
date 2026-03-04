import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if sum(p) != 1:
        raise ValueError
    e = 0
    for x_i, p_i in zip(x, p):
        e = e + x_i*p_i
        
    return e
    pass
