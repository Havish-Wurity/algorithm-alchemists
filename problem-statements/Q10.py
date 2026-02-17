def organize_scores(scores, descending):
    sorted_scores = scores.copy()
    
    sorted_scores.sort(reverse=descending)
    
    return sorted_scores

