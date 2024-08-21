def some_but_not_all(seq, pred): 
    # check through each sequence to see if any elements satisfy the predicate, but return "False" if they all do
    result = any(pred(x) for x in seq) and not all(pred(x) for x in seq)
    return result