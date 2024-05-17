import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for line in sys.stdin:
    M, N = map(int, line.split())
    common_divisor = gcd(M, N)
    M_divided = M // common_divisor
    N_divided = N // common_divisor
    if M_divided % 2 == 0 or N_divided % 2 == 0:
        common_divisor = 0
    print(common_divisor)
