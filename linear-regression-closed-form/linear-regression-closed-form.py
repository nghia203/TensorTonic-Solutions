import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)

    product1 = np.linalg.inv(X.T @ X)
    product2 = X.T @ y
    return product1 @ product2
    pass