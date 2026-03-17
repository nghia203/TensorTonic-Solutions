import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    predictions = np.asarray(predictions)
    final_vote = np.apply_along_axis(
        lambda x: np.bincount(x).argmax(), 
        axis = 0, 
        arr = predictions
    )
    return final_vote.tolist()