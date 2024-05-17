import sys

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        
        if x_root == y_root:
            return
        
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

def sieve_of_eratosthenes(n):
    primes = []
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    
    for p in range(2, n+1):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n+1, p):
                sieve[i] = False
    
    return primes

def prime_factors(n, primes):
    factors = set()
    for p in primes:
        if p*p > n:
            break
        while n % p == 0:
            factors.add(p)
            n //= p
    if n > 1:
        factors.add(n)
    return factors

def count_sets(A, B, P):
    primes = sieve_of_eratosthenes(P)
    ds = DisjointSet(B - A + 2)
    for i in range(A, B+1):
        factors = prime_factors(i, primes)
        for j in range(i+1, B+1):
            if any(factor in prime_factors(j, primes) for factor in factors):
                ds.union(i - A + 1, j - A + 1)
    
    unique_sets = set()
    for i in range(B - A + 2):
        unique_sets.add(ds.find(i))
    
    return len(unique_sets) - 1  # Subtract 1 to exclude the extra set for ungrouped elements

def main():
    for line in sys.stdin:
        C = int(line.strip())
        for case in range(C):
            A, B, P = map(int, input().split())
            sets = count_sets(A, B, P)
            print(f"Case #{case+1}: {sets}")

if __name__ == "__main__":
    main()
