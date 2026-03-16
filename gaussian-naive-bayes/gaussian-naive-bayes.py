import numpy as np

def gaussian_naive_bayes(X_train, y_train, X_test):
    """
    Predict class labels for test samples using Gaussian Naive Bayes.
    """
    # Write code here
    X_train, y_train, X_test = map(np.asarray, [X_train, y_train, X_test])
    classes = np.unique(y_train)
    n_test = X_test.shape[0]
    stats = {}
    
    for c in classes:
        X_c = X_train[y_train == c]
        stats[c] = {
            "mean": np.mean(X_c, axis = 0),
            "var": np.var(X_c, axis = 0) + 1e-9,
            "prior": X_c.shape[0] / X_train.shape[0]
        }
        
    log_posteriors = np.zeros((n_test, len(classes)))

    for i, c in enumerate(classes):
        mean = stats[c]["mean"]
        var = stats[c]["var"]
        prior = stats[c]["prior"]
        
        exponent = -0.5 * np.sum(((X_test - mean) ** 2) / var, axis=1)
        log_prob = -0.5 * np.sum(np.log(2 * np.pi * var))
        
        log_posteriors[:, i] = prior + log_prob + exponent

    return classes[np.argmax(log_posteriors, axis=1)].tolist()