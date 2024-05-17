import sys

MOD = 10**9 + 7

def sieve(n):
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n+1) if primes[i]]

def prime_factors(n, primes):
    factors = {}
    for prime in primes:
        if prime * prime > n:
            break
        while n % prime == 0:
            n //= prime
            factors[prime] = factors.get(prime, 0) + 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def product_of_divisors(sequence):
    primes = sieve(max(sequence))
    factors_counts = {}
    for num in sequence:
        factors = prime_factors(num, primes)
        for factor, count in factors.items():
            factors_counts[factor] = max(factors_counts.get(factor, 0), count)
    product = 1
    for count in factors_counts.values():
        product = (product * (count + 1)) % MOD
    return product

def main():
    for line in sys.stdin:
        n = int(line)
        sequence = list(map(int, input().split()))
        result = product_of_divisors(sequence)
        print(result)

if __name__ == "__main__":
    main()
