import sys
from math import gcd

def extended_gcd(a, b):
    if b == 0:
        return (1, 0)
    else:
        x, y = extended_gcd(b, a % b)
        return (y, x - (a // b) * y)

def find_smallest_AB(R, S, Q):
    # Compute Bezout's coefficients a and b
    a, b = extended_gcd(R, S)

    # Rescale a and b by Q
    a *= Q
    b *= Q

    # Adjust a and b for specific conditions
    if R < 0:
        a = -a
    if S > 0:
        b = -b

    # If Q is negative, adjust a and b accordingly
    if Q < 0:
        a, b = -a, -b

    # Ensure both A and B are positive
    min_value = min(a, b)
    a += (1 - min_value)
    b += (1 - min_value)

    return a, b

# Read input
for line in sys.stdin:
    T = int(line.strip())
    for _ in range(T):
        R, S, Q = map(int, input().split())
        A, B = find_smallest_AB(R, S, Q)
        print(A, B)
