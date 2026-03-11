import numpy as np

def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    log_p = 0
    for i in range(len(prob_distributions)):
        p = prob_distributions[i][actual_tokens[i]]
        log_p += np.log(p)
    return np.exp(-log_p / len(actual_tokens))