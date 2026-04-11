import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    left, count_left = np.unique(y_left, return_counts = True)
    right, count_right = np.unique(y_right, return_counts = True)
    n_l = len(y_left)
    n_r = len(y_right)
    n = n_l + n_r
    if n == 0:
        return 0.0
    if n_l == 0:
        gini_l = 0
    else:
        gini_l = 1 - np.sum((count_left / n_l) ** 2)
    if n_r == 0:
        gini_r = 0
    else:
        gini_r = 1 - np.sum((count_right / n_r) ** 2)
    return n_l / n * gini_l + n_r / n * gini_r