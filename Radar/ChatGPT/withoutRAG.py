import math

# Function to find the greatest common divisor using Euclid's algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find the least common multiple
def lcm(a, b):
    return a * b // gcd(a, b)

# Function to find the modular inverse using Extended Euclidean Algorithm
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function to solve the problem
def smallest_distance(m, x, y):
    M = lcm(lcm(m[0], m[1]), m[2])
    result = 0
    for i in range(3):
        M_i = M // m[i]
        inv = mod_inverse(M_i, m[i])
        result += x[i] * M_i * inv

    min_z = result % M
    for i in range(3):
        min_z = max(min_z, x[i] - y[i])
        min_z = min(min_z, x[i] + y[i], x[i] + m[i] - y[i])
    return min_z

# Sample input reading
m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

# Calculate and print the result
print(smallest_distance(m, x, y))
