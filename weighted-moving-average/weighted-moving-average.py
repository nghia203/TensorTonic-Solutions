def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here
    window_weight = []
    n = len(weights)
    for i in range(len(values) - n + 1):
        window = values[i : i + n]

        weighted_sum = sum(v * w for v, w in zip(window, weights))

        window_weight.append(weighted_sum / sum(weights))
    return window_weight