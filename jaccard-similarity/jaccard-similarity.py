import numpy as np
def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    set_a = set(set_a)
    set_b = set(set_b)
    intersection = len(set_a.intersection(set_b))
    union = len(set_b.union(set_a))

    if union == 0:
        return 0
    return intersection / union