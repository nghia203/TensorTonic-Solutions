def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    # Write code here
    wealth = 1.0
    w = []
    for r in returns:
        wealth = wealth * (1 + r)
        w.append(wealth - 1)
    return w