def double_every_other(lst):
    evens = lst[1::2]
    evens_doubled = [x * 2 for x in evens]
    lst[1::2] = evens_doubled
    return lst