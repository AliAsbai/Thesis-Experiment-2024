import sys

def check_power(num, c):
    result = 1
    for _ in range(c):
        result *= num
        result %= 1000  # Only keep last 3 digits for efficiency
    return result

def find_secret_code(numbers):
    for c in range(2, 10001):  # c > 1
        valid = True
        for num in numbers:
            if check_power(num, c) % num != 0:
                valid = False
                break
        if valid:
            return c
    return -1

if __name__ == "__main__":
    # Read input
    N = int(input())
    numbers = list(map(int, input().split()))

    # Find and print the secret code
    print(find_secret_code(numbers))
