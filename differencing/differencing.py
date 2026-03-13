def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here
    for i in range(0, order):
        series = [series[j] - series[j-1] for j in range(1, len(series))]
    return series