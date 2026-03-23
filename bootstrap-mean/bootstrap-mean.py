import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    # Write code here
    if rng is None:
        rng = np.random.default_rng()
    x = np.asarray(x)
    n = len(x)

    resamples = rng.choice(x, size=(n_bootstrap, n), replace = True)

    boot_means = np.mean(resamples, axis = 1)

    lower_p = (1 - ci) / 2 * 100
    upper_p = (1 + ci) / 2 * 100
    
    lower = np.percentile(boot_means, lower_p)
    upper = np.percentile(boot_means, upper_p)

    return boot_means, lower, upper
    pass
