def order_weight(strng):
    strng_split = strng.split(' ')
    sums = []
    for n in strng_split:
        sum_of_digits = sum(int(digit) for digit in n)
        sums.append(sum_of_digits)
    zipped_lists = zip(sums, strng_split)
    sorted_lists = sorted(zipped_lists)
    sorted_strng_split = [item[1] for item in sorted_lists]
    sorted_strng_split = ', '.join(sorted_strng_split)
    cleaned_strng = sorted_strng_split.replace(',', '')
    return cleaned_strng