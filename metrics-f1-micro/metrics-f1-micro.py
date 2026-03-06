def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    tp = fn = 0
    for y_1, y_2 in zip(y_true, y_pred):
        if y_1 == y_2:
            tp = tp + 1
        else:
            fn = fn + 1
    return tp* 2 / (tp*2 + fn* 2)
    pass