def seasonal_average(series, period):
    """
    Compute the average value for each position in the seasonal cycle.
    """
    # Write code here
    n = len(series)

    sum_avg = [0.0] * period
    counts = [0] * period
    for start_idx in range(0, len(series), period):
            for p in range(period):
                cur_idx = start_idx + p

                if cur_idx < n:
                    val = series[cur_idx]
                    sum_avg[p] += val
                    counts[p] += 1
    return [sum_avg[p] / counts[p] if counts[p] > 0 else 0.0 for p in range(period)]