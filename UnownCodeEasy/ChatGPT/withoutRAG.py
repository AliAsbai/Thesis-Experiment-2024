def check_power(num, c):
    result = num
    for _ in range(c - 1):
        result *= num
        result %= 1000000000  # To avoid overflow, only keep the last 9 digits
    return result % 1000000000  # Return only the last 9 digits

def find_secret_code(N, numbers):
    for c in range(2, 10001):  # Start checking from c = 2 up to 10000
        valid = True
        for num in numbers:
            if check_power(num, c) != num:
                valid = False
                break
        if valid:
            return c
    return -1

# Input reading
N = int(input())
numbers = list(map(int, input().split()))

# Finding and printing the secret code
print(find_secret_code(N, numbers))
