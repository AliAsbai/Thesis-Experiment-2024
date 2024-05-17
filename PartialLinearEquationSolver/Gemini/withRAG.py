import sys

def gaussian_elimination(A, b):
    n = len(A)

    # Forward elimination
    for k in range(n - 1):
        # Check for zero pivot
        if abs(A[k][k]) < 1e-9:
            # Find a non-zero pivot in the column below
            pivot_row = k + 1
            while pivot_row < n and abs(A[pivot_row][k]) < 1e-9:
                pivot_row += 1

            # Swap rows if necessary
            if pivot_row < n:
                A[k], A[pivot_row] = A[pivot_row], A[k]
                b[k], b[pivot_row] = b[pivot_row], b[k]
            else:
                # Inconsistent system
                return None

        # Partial pivoting (assuming the pivot is non-zero now)
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k + 1, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]

    # Back substitution
    x = [0] * n
    for k in range(n - 1, -1, -1):
        # Check for zero pivot
        if abs(A[k][k]) < 1e-9:
            # Inconsistent system (check for non-zero constant term only for rows above the last one)
            if k < n - 1 and b[k] != 0:
                return None
            else:  # Infinitely many solutions (all variables after k are free)
                x[k] = "?"
                continue

        x[k] = (b[k] - sum(A[k][j] * x[j] for j in range(k + 1, n))) / A[k][k]

    return x

while True:
    line = sys.stdin.readline()
    if not line:
        break

    n = int(line)
    if n == 0:
        break

    A = []
    for _ in range(n):
        A.append(list(map(float, sys.stdin.readline().split())))
    b = list(map(float, sys.stdin.readline().split()))

    x = gaussian_elimination(A, b)

    if x is None:
        print("inconsistent")
    else:
        for val in x:
            print("%.2f" % val if not isinstance(val, str) else val),
        print()
