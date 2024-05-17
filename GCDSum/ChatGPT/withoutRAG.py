def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def compute_sum(N):
    total_sum = 0
    for i in range(1, N + 1):
        if N % i == 0:
            for j in range(1, N + 1):
                if N % j == 0:
                    total_sum += gcd(i, j)
    return total_sum

# Reading input from the user
N = int(input().strip())

# Computing the sum
result = compute_sum(N)

# Outputting the result
print(result)
