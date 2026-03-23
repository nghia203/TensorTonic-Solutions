import numpy as np

def naive_bayes_bernoulli(X_train, y_train, X_test, alpha = 1.0):
    """
    Compute log-likelihood P(y|x) for Bernoulli Naive Bayes.
    """
    # Write code here
    X_train = np.asarray(X_train)
    y_train = np.asarray(y_train)
    X_test = np.asarray(X_test)

    n_samples, n_features = X_train.shape
    classes = np.unique(y_train)
    n_classes = len(classes)
    n_test = X_test.shape[0]

    log_likelihood = np.zeros((n_test, n_classes))

    for idx, c in enumerate(classes):
        X_c = X_train[y_train == c]

        prior_c = len(X_c) / n_samples
        log_prior_c = np.log(prior_c)

        p_i = (np.sum(X_c, axis=0) + alpha) / (len(X_c) + 2 * alpha)

        log_prob_x_given_c = X_test @ np.log(p_i) + (1 - X_test) @ np.log(1 - p_i)
        log_likelihood[:, idx] = log_prob_x_given_c + log_prior_c

    return log_likelihood
    pass