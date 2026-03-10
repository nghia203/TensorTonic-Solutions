import numpy as np
from collections import Counter
def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    counts = Counter(y_train)
    X_test = [counts.most_common(1)[0][0] for test in X_test]
    return X_test
    pass