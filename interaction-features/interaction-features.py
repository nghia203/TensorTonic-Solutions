def interaction_features(X):
    """
    """
    result = []
    
    for row in X:
        new_row = list(row)
        n = len(row)
        
        for i in range(n):
            for j in range(i + 1, n):
                product = row[i] * row[j]
                new_row.append(product)
        
        result.append(new_row)
        
    return result
