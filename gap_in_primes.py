import gmpy2

def gap(g, m, n):
    for i in range(m,n+1):
        if gmpy2.is_prime(i):
            test = i + g
            if gmpy2.is_prime(test) and all([not gmpy2.is_prime(j) for j in range(i + 1, test)]):
                return [i, test]
            else:
                m = i