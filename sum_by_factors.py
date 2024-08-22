import gmpy2
from math import sqrt

def prime_factors(n):
    """Returns a list of prime factors of a given number n."""
    factors = []
    abs_n = abs(n)
    
    # Check divisibility by 2 first
    if abs_n % 2 == 0:
        factors.append(2)
        while abs_n % 2 == 0:
            abs_n //= 2

    # Check divisibility by odd numbers from 3 to sqrt(abs_n)
    for i in range(3, int(sqrt(abs_n)) + 1, 2):
        if abs_n % i == 0 and gmpy2.is_prime(i):
            factors.append(i)
            while abs_n % i == 0:
                abs_n //= i

    # If abs_n is still greater than 2, it must be prime
    if abs_n > 2:
        factors.append(abs_n)

    return factors

def sum_for_list(lst):
    # Dictionary to store sums for each prime
    sums_for_primes = {}

    # Iterate through each number in the list
    for num in lst:
        # Get the prime factors of the number
        factors = prime_factors(num)
        
        # Update sums for each prime factor
        for prime in factors:
            if prime in sums_for_primes:
                sums_for_primes[prime] += num
            else:
                sums_for_primes[prime] = num
        
    # Sort and return the result
    return sorted([[key, value] for key, value in sums_for_primes.items()])