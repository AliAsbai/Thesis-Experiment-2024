import sys

def solve_system(n, matrix, b):
    EPSILON = 1e-10

    for i in range(n):
        # Find pivot row and swap if necessary
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k
        if abs(matrix[max_row][i]) < EPSILON:
            return "inconsistent"  # System is inconsistent

        # Swap rows
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        b[i], b[max_row] = b[max_row], b[i]

        # Perform forward elimination
        for j in range(i + 1, n):
            pivot = matrix[i][i]
            factor = matrix[j][i] / pivot
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]
            b[j] -= factor * b[i]

    # Perform back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        pivot = matrix[i][i]
        if abs(pivot) < EPSILON:
            if abs(b[i]) < EPSILON:
                x[i] = "?"
            else:
                return "inconsistent"  # System is inconsistent
        else:
            x[i] = b[i] / pivot
            for j in range(i + 1, n):
                x[i] -= matrix[i][j] * x[j] / pivot

    return x

def main():
    for line in sys.stdin:
        n = int(line)
        if n == 0:
            break

        matrix = []
        for _ in range(n):
            row = list(map(float, sys.stdin.readline().strip().split()))
            matrix.append(row)

        b = list(map(float, sys.stdin.readline().strip().split()))

        solution = solve_system(n, matrix, b)
        if isinstance(solution, str):
            print(solution)
        else:
            print(" ".join(f"{value:.2f}" if isinstance(value, float) else value for value in solution))

if __name__ == "__main__":
    main()
