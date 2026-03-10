def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Write code here
    unseen_scores = [(scores[i], i) for i in range(len(scores)) if i not in rated_indices]
    unseen_scores.sort(key = lambda x: x[0], reverse = True)
    top_k = [unseen_score[1] for unseen_score in unseen_scores[:k]]
    return top_k
    