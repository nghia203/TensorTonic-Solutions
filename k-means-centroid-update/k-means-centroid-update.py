import numpy as np

def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here
    points = np.asarray(points)
    assignments = np.asarray(assignments)
    k_update = np.zeros((k, points.shape[1]))
    for i in range(k):
        cluster = points[assignments == i]
        if len(cluster) > 0:
            k_update[i] = cluster.mean(axis=0)
        else:
            k_update[i] = np.zeros(points.shape[1])
    return k_update.tolist()
            