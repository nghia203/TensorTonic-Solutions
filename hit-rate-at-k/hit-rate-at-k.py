import numpy as np
def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    u = len(recommendations)
    if u == 0:
        return 0.0
    hit = 0
    for i in range(u):
        top_k = recommendations[i][:k]
        if any(item in top_k for item in ground_truth[i]):
            hit += 1
    return hit / u