def find_largest_d(S):
    S_sorted = sorted(S)
    max_d = None

    for i in range(len(S_sorted) - 1, -1, -1):
        a = S_sorted[i]
        for j in range(i - 1, -1, -1):
            b = S_sorted[j]
            complement = a + b
            if complement in S and complement > a and complement > b:
                max_d = complement
                break
        if max_d is not None:
            break

    return max_d if max_d is not None else "no solution"


# Read input
N = int(input())
S = set()
for _ in range(N):
    S.add(int(input()))

# Find and print the largest d
print(find_largest_d(S))
