import sys
from collections import Counter

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

def calculate_points(X):
    factors = prime_factors(X)
    factor_count = Counter(factors)
    points = 1
    for count in factor_count.values():
        points *= (count + 1)
    return points

for line in sys.stdin:
    X = int(line)
    points = calculate_points(X)
    print(points - 1)  # Subtract 1 because the player needs to provide k distinct positive integers, not including 1 itself
