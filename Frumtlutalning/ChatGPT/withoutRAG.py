def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_between(a, b):
    count = 0
    for num in range(a, b + 1):
        if is_prime(num):
            count += 1
    return count

# Input
a, b = map(int, input().split())

# Output
print(count_primes_between(a, b))
