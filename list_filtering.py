def filter_list(l):
    'return a new list with the strings filtered out'
    filtered_l = [item for item in l if isinstance(item, int)]
    return filtered_l