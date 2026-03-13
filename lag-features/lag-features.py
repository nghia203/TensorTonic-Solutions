def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    # Write code here
    max_lag = max(lags)
    features = []
    for t in range(max_lag, len(series)):
        row = [series[t - lag] for lag in lags]
        features.append(row)
    return features