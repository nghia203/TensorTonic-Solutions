import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    if len(A) == 1 & len(A[0]) == 1:
        return A[0][0]
    trace = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i == j:
                trace = trace + A[i][j]
    return trace
    pass
