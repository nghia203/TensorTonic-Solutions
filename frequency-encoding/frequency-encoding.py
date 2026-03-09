def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here

    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return [counts[value] / len(values) for value in values]
    