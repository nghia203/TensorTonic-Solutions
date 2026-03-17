import numpy as np

def decision_tree_split(X, y):
    """
    Find the best feature and threshold to split the data.
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)
    n_samples, n_features = X.shape

    if n_samples <= 1:
        return None, None
        
    def gini(labels):
        if len(labels) == 0:
            return 0
        p_i = np.bincount(labels)
        p_k = p_i / len(labels)
        return 1 - np.sum(p_k**2)

    best_gini = float('inf')
    best_threshold = None
    best_feature = None
    
    for feature in range(n_features):
        unique = np.unique(X[:, feature])
        midpoints = (unique[:-1] + unique[1:]) / 2
        for threshold in midpoints:
            left_mask = X[:, feature] <= threshold
            right_mask = ~left_mask

            y_left, y_right = y[left_mask], y[right_mask]
    
            gini_l = gini(y_left)
            gini_r = gini(y_right)
            weighted_gini = (len(y_left) * gini_l + len(y_right) * gini_r) / n_samples

            if weighted_gini < best_gini:
                best_gini = weighted_gini
                best_threshold = threshold
                best_feature = feature
    return [best_feature, best_threshold]
            

        
        
    