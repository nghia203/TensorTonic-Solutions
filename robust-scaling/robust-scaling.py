import numpy as np
def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    # Write code here
    values = np.asarray(values)
    median = np.median(values)
    if len(values) % 2 == 1:
        q1 = np.percentile(values, 25, method='weibull')
        q3 = np.percentile(values, 75, method='weibull')
    else:
        q1 = np.percentile(values, 25, method='inverted_cdf')
        q3 = np.percentile(values, 75, method='inverted_cdf')
    iqr = q3 - q1
    if iqr == 0:
        return values - median
    return (values - median) / iqr