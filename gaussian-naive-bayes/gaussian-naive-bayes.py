import numpy as np

def gaussian_naive_bayes(X_train, y_train, X_test):
    """
    Predict class labels for test samples using Gaussian Naive Bayes.
    """
    # Write code here
    X_train = np.asarray(X_train)
    y_train = np.asarray(y_train)
    X_test = np.asarray(X_test)
    
    classes = np.unique(y_train)
    n_features = X_train.shape[1]

    stats = {}
    for c in classes:
        X_c = X_train[y_train == c]
        stats[c] = {
            "mean": np.mean(X_c, axis = 0),
            "var": np.var(X_c, axis = 0) + 1e-9,
            "prior": X_c.shape[0] / X_train.shape[0]
        }
    def cal_log_likelihood(x, mean, var):
        exp = -((x - mean) ** 2) / (var * 2)
        log_cal = -np.log(2 * np.pi * var) / 2 + exp
        return np.sum(log_cal)

    prediction = []
    for x in X_test:
        posteriors = []
        for c in classes:
            prior = np.log(stats[c]["prior"])
            likelihood = cal_log_likelihood(x, stats[c]["mean"], stats[c]["var"])
            posteriors.append(prior + likelihood)

        prediction.append(classes[np.argmax(posteriors)])

    return prediction
        
    