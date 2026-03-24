import numpy as np
def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here
    if n_items == 0:
        return 0.0
    recommendations = np.concatenate(recommendations)

    values = np.unique(recommendations)

    counts = len(values)

    return float(np.sum(counts) / n_items)
    