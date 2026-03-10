import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    rater1 = np.asarray(rater1)
    rater2 = np.asarray(rater2)
    n = len(rater1)
    
    p0 = np.sum(rater1 == rater2) / n
    
    categories = np.unique(np.concatenate([rater1, rater2]))
    pe = 0
    for cat in categories:
        prob1 = np.sum(rater1 == cat) / n
        prob2 = np.sum(rater2 == cat) / n

        pe += (prob1 * prob2)
    if pe == 1.0:
        return 1.0
    return (p0 - pe) / (1 - pe)
    pass