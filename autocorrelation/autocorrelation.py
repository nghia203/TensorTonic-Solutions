import numpy as np
def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    # Write code here
    mean = np.mean(series)

    var = np.var(series)
    sum = []
    if var == 0:
        return [1.0] + [0.0] * max_lag

    for k in range(max_lag + 1):
        actual_series = series[:len(series)-k] - mean
        lagged_series = series[k:] - mean
        
        covariance_k = np.sum(actual_series * lagged_series) / len(series)

        sum.append(covariance_k / var)

    return sum