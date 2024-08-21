# original
def dig_pow(n, p):
    n_string = str(n)
    powers = [i for i in range(p, p + len(n_string))]
    sum_of_powers = sum([int(num) ** power for num,power in zip(n_string, powers)])
    if sum_of_powers % n == 0:
        return sum_of_powers // n
    else:
        return -1

# cut down version
def dig_pow(n, p):
    sum_of_powers = sum([int(num) ** power for num,power in zip(str(n), [i for i in range(p, p + len(str(n)))])])
    if sum_of_powers % n == 0:
        return sum_of_powers // n
    else:
        return -1