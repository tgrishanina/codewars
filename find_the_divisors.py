import gmpy2

def divisors(integer):
    if gmpy2.is_prime(integer):
        return f"{integer} is prime"
    else:
        factors = [f for f in range(2, integer) if integer % f == 0]
        return factors