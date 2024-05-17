from math import sqrt


class DisjointSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] > self.rank[root_y]:
            self.parents[root_y] = root_x
        else:
            self.parents[root_x] = root_y
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_prime_factors(n, p):
    factors = set()
    i = 2
    while i <= n:  # changed from i * i <= n to i <= n
        if n % i == 0:
            if i >= p:
                factors.add(i)
            n //= i
        i += 1
    return factors


def solve(a, b, p):
    dsu = DisjointSet(b - a + 1)
    min_indices = {f: float('inf') for f in range(p, b + 1)}  # dictionary to store minimum indices for factors

    for i in range(a, b + 1):
        factors = get_prime_factors(i, p)
        for f in factors:
            min_indices[f] = min(min_indices[f], i - a)  # update minimum index for the factor
        for f in factors:
            if min_indices[f] != i - a:  # check if current index is not the minimum
                dsu.union(i - a, min_indices[f])

    return len(set(dsu.find(i - a) for i in range(a, b + 1)))


def main():
    num_cases = int(input())
    for case in range(1, num_cases + 1):
        a, b, p = map(int, input().split())
        num_sets = solve(a, b, p)
        print(f"Case #{case}: {num_sets}")


if __name__ == "__main__":
    main()
