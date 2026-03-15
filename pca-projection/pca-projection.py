import numpy as np

def pca_projection(X, k):
    """
    Project data onto the top-k principal components.
    """
    # Write code here
    X = np.asarray(X)
    if X.ndim != 2 or k <= 0:
        return None
    X_centered = X - np.mean(X, axis = 0)
    cov = (X_centered.T @ X_centered) / (len(X) - 1)
    eigen_vals, eigen_vecs = np.linalg.eigh(cov)
    
    idx = np.argsort(eigen_vals)[::-1]
    top_k_eigenvecs = eigen_vecs[:, idx[:k]]
    
    return X_centered @ top_k_eigenvecs
    return 