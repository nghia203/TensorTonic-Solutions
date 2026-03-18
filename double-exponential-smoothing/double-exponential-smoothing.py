def double_exponential_smoothing(series, alpha, beta):
    """
    Apply Holt's linear trend method and return the level values.
    """
    # Write code here
    result = [series[0]]
    level = series[0]
    trend = series[1] - series[0]
    for t in range(1, len(series)):
        new_level = alpha * series[t] + (1 - alpha) * (level + trend) 
        new_trend = beta * (new_level - level) + (1 - beta) * trend
        result.append(new_level)
        trend = new_trend
        level = new_level
    return result