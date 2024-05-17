import math

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

def find_AB(R, S, Q):
    gcd, x, y = extended_gcd(R, S)
    A = Q * x // gcd
    B = Q * y // gcd
    return A, B

def find_smallest_AB(R, S, Q):
    A, B = find_AB(R, S, Q)
    # Ensure A and B are positive
    while A <= 0 or B <= 0:
        A += S // math.gcd(R, S)
        B += R // math.gcd(R, S)
    return A, B

def main():
    T = int(input())
    for _ in range(T):
        R, S, Q = map(int, input().split())
        A, B = find_smallest_AB(R, S, Q)
        print(A, B)

if __name__ == "__main__":
    main()
