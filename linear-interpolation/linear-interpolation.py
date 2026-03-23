def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    # Write code here
    filled_values = values
    i = 0
    while i < len(values):
        if values[i] is None:
            left_idx = i - 1

            right_idx = i
            while right_idx < len(values) and values[right_idx] is None:
                right_idx += 1
                
            for t in range(left_idx + 1, right_idx):
                filled_values[t] = values[left_idx] + (t - left_idx) / (right_idx - left_idx) * (values[right_idx] - values[left_idx])
            i = right_idx
        else:
            i += 1
    return filled_values
            
            
        