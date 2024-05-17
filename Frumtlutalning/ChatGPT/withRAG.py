import sys
import math

# Generate primes using the sieve of Eratosthenes
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(2, limit + 1) if sieve[i]]

# Generate primes within the specified range using segmented sieve
def segmented_sieve(a, b):
    limit = int(math.sqrt(b)) + 1
    primes = sieve_of_eratosthenes(limit)
    segment_size = b - a + 1
    is_prime = [True] * segment_size

    for p in primes:
        start = max(p * p, (a + p - 1) // p * p)
        for j in range(start, b + 1, p):
            is_prime[j - a] = False

    count = sum(1 for x in is_prime if x)
    if a <= 1:
        count -= 1

    return count

if __name__ == "__main__":
    for line in sys.stdin:
        a, b = map(int, line.split())
        print(segmented_sieve(a, b))
