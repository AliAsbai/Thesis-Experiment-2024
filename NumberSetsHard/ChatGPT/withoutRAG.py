import math

def prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)
    return factors

def count_sets(A, B, P):
    sets = {}
    for num in range(A, B + 1):
        sets[num] = num
    
    for num in range(A, B + 1):
        for other_num in range(num + 1, B + 1):
            if len(prime_factors(num).intersection(prime_factors(other_num))) >= P:
                root1 = find_root(sets, num)
                root2 = find_root(sets, other_num)
                if root1 != root2:
                    sets[root2] = root1
    
    unique_roots = set()
    for num in sets.values():
        unique_roots.add(find_root(sets, num))
    
    return len(unique_roots)

def find_root(sets, num):
    if sets[num] != num:
        sets[num] = find_root(sets, sets[num])
    return sets[num]

if __name__ == "__main__":
    C = int(input().strip())
    for case in range(1, C + 1):
        A, B, P = map(int, input().split())
        result = count_sets(A, B, P)
        print(f"Case #{case}: {result}")
