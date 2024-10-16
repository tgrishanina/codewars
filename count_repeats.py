# Write a function that returns the count of characters that have to be removed in order to get a string with no consecutive repeats.
def count_repeats(txt):
    result = [txt[0]]  # Initialize with the first character
    for char in range(1, len(txt)):
        if txt[char] != txt[char - 1]:  # Compare current with the previous character
            result.append(txt[char])
    
    new_string = ''.join(result)
    return len(txt) - len(new_string)