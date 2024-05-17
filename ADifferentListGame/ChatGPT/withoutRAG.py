def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def count_points(X):
    factors = prime_factors(X)
    distinct_factors = set(factors)
    return len(distinct_factors)

# Input
X = int(input())

# Output
print(count_points(X))
