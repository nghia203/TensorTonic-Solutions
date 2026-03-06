def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    count = {}
    for sentence in sentences:
        for word in sentence:
            count[word] = count.get(word, 0) + 1
    return count
    pass