MOD = 10**9 + 7

# Function to compute prime factorization
def prime_factorization(n):
    factors = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
            factors[i] = factors.get(i, 0) + 1
        i += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

# Function to count divisors of the product
def count_divisors_of_product(numbers):
    max_factors = {}  # Dictionary to store maximum power of each prime factor
    for num in numbers:
        factors = prime_factorization(num)
        for factor, power in factors.items():
            max_factors[factor] = max(max_factors.get(factor, 0), power)
    
    divisors = 1
    for power in max_factors.values():
        divisors *= (power + 1)
        divisors %= MOD
    
    return divisors

# Input reading
n = int(input())
sequence = list(map(int, input().split()))

# Compute and output the result
print(count_divisors_of_product(sequence))
