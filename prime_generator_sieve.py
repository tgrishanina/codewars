import math

class Primes:
    @staticmethod
    def stream():
        yield 2  # Yield the first prime number
        segment_size = 10**6  # Size of each segment to sieve

        # Store small primes to use for marking composites in larger segments
        small_primes = []
        limit = 10000  # Increased initial limit to find small primes
        is_prime = [True] * (limit + 1)

        # Simple sieve of Eratosthenes to find small primes up to `limit`
        for num in range(2, limit + 1):
            if is_prime[num]:
                small_primes.append(num)
                for multiple in range(num * num, limit + 1, num):
                    is_prime[multiple] = False

        # Start sieving larger segments
        start = 3  # Starting point for larger segments

        while True:
            # Create a sieve for the current segment
            sieve = [True] * segment_size
            end = start + segment_size  # End of the current segment

            # Use small primes to mark composites in the current segment
            for prime in small_primes:
                # Calculate the first multiple of prime in the current segment
                first_multiple = max(prime * prime, start + (prime - start % prime) % prime)
                for multiple in range(first_multiple, end, prime):
                    sieve[multiple - start] = False

            # Yield primes found in the current segment
            for i in range(segment_size):
                number = start + i
                if number >= end:
                    break
                if sieve[i] and number > 1:  # Ensure we only yield numbers greater than 1
                    yield number

            # Move to the next segment
            start = end


# better way (using gmpy2)
import gmpy2
class Primes:
    @staticmethod
    def stream():
        n = 2
        while True:
            yield n
            n = gmpy2.next_prime(n)