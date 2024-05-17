import sys

def divisor_sum(n):
    total_sum = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            total_sum += i
            if i != n // i:
                total_sum += n // i
    return total_sum

def sum_gcd(n):
    total_sum = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            total_sum += i * divisor_sum(n // i)
    return total_sum

for line in sys.stdin:
    N = int(line)
    result = sum_gcd(N)
    print(result)
