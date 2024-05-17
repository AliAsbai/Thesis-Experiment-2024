def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def count_equal_area_blocks(M, N):
    if M == 1 or N == 1:
        return 0

    total_blocks = M * N

    # Finding the greatest common divisor of M and N
    common_divisor = gcd(M, N)

    # Number of blocks cut into two equal parts will be the sum of M and N - 1
    return (M + N - common_divisor)

# Taking input
M, N = map(int, input().split())

# Printing the result
print(count_equal_area_blocks(M, N))
