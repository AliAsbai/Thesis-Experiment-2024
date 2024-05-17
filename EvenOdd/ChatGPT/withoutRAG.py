MOD = 10**9 + 7

def f(X):
    iterations = 0
    while X != 1:
        if X % 2 == 0:
            X //= 2
        else:
            X += 1
        iterations += 1
    return iterations

def power_mod(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

def compute_sum(L, R):
    total_sum = 0
    current = L
    while current <= R:
        next_power_of_two = 1
        while next_power_of_two * 2 <= current:
            next_power_of_two *= 2
        total_sum = (total_sum + (next_power_of_two * f(next_power_of_two))) % MOD
        current = next_power_of_two + 1
    return total_sum

# Input
L, R = map(int, input().split())

# Output
print(compute_sum(L, R))
