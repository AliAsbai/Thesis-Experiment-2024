import sys

def find_largest_d(S):
    S = sorted(S)  # Sort the set of integers

    largest_d = S[-1]  # Largest element in S

    # Iterate through all elements in S except the largest one
    for i in range(len(S) - 1):
        a = S[i]
        for j in range(i + 1, len(S)):
            b = S[j]
            # Calculate the remaining value needed to reach the largest_d
            c = largest_d - (a + b)
            if c in S and c != a and c != b:
                return largest_d
    return "no solution"

if __name__ == "__main__":
    S = set()
    for line in sys.stdin:
        S.add(int(line.strip()))

    result = find_largest_d(S)
    print(result)
