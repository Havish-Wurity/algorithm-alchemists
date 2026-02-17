def generate_threes(start, end):
    if start >= end:
        return []
    
    return list(range(start, end, 3))
