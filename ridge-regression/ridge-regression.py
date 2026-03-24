import numpy as np

def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)

    r1 = X.T @ X
    d = r1.shape[0]
    
    I = np.eye(d)

    inv_matrix = np.linalg.inv(r1 + lam * I)

    r2 = X.T @ y

    w = inv_matrix @ r2

    return w
    
    
    