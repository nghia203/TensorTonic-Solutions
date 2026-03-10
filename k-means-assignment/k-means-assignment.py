import numpy as np
def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    points = np.asarray(points)
    centroids = np.asarray(centroids)
    assignments = []
    for p in points:
        distance = np.sum((p - centroids)**2, axis = 1)
        closest = np.argmin(distance)
        assignments.append(int(closest))
    return assignments