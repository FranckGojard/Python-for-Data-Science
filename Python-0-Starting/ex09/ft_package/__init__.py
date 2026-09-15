def count_in_list(lst, target):
    """Count how many times target appears in lst."""
    result = 0
    for element in lst:
        if element == target:
            result +=1
    return result
        