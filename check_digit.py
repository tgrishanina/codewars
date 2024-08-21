def check_digit(number, index1, index2, digit):
    # change number and digit to strings before checking
    return str(digit) in str(number)[index2 : index1 + 1] or str(digit) in str(number)[index1 : index2 +1]
