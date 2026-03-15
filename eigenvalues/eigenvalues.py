import numpy as np

def calculate_eigenvalues(matrix):

    if matrix is None or len(matrix) == 0:
        return None

    try:
        matrix = np.array(matrix)
        
        if matrix.size == 0:
            return None
        if matrix.dtype == object:
            return None
            
    except (ValueError, TypeError):
        return None

    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return None

    try:
        eig_vals = np.linalg.eigvals(matrix)
        
        idx = np.lexsort((eig_vals.imag, eig_vals.real))
        
        return eig_vals[idx]
        
    except np.linalg.LinAlgError:
        return None