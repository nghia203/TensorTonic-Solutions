
def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    mean_rating = [(row[1] / (row[1] + min_votes)) * row[0] + (min_votes / (row[1] + min_votes)) * global_mean for row in items]
    
    return mean_rating

    