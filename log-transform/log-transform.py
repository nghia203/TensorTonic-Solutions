import math
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here

    y = [math.log1p(x) for x in values]
    return y
    