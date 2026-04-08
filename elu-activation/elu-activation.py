def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    import numpy as np
    x = np.asarray(x)
    x = np.where(x> 0, x, alpha * (np.exp(x) - 1))
    return x.tolist()