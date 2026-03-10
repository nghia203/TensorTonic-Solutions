def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    stopwords_set = set(stopwords)
    removed = []
    for word in tokens:
        removed = [word for word in tokens if word not in stopwords_set]

    return removed
    pass