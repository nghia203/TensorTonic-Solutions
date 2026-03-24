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

    w = np.linalg.solve(r1 + I * lam, X.T @ y)

    return w
    
    
    