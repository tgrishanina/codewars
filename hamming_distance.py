def hamming(a, b):
    count = 0
    # Iterate through the length of the shorter string
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            count += 1
    # Add the difference in lengths to the count
    count += abs(len(a) - len(b))
    return count