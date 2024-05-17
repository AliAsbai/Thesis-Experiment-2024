def gaussian_elimination(A, b):
    n = len(A)

    # Forward Elimination
    for i in range(n):
        if A[i][i] == 0:
            return "inconsistent"
        for j in range(i+1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= ratio * A[i][k]
            b[j] -= ratio * b[i]

    # Back Substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        if A[i][i] == 0:
            return "inconsistent"
        x[i] = b[i] / A[i][i]
        for j in range(i):
            b[j] -= A[j][i] * x[i]

    return x


def solve_system_of_equations():
    while True:
        n = int(input())
        if n == 0:
            break

        A = []
        for _ in range(n):
            A.append(list(map(float, input().split())))

        b = list(map(float, input().split()))

        solution = gaussian_elimination(A, b)

        if solution == "inconsistent":
            print("inconsistent")
        else:
            for val in solution:
                if abs(val) < 1e-9:  # considering values very close to zero as zero
                    print("0.00", end=" ")
                else:
                    print("{:.2f}".format(val), end=" ")
            print()


if __name__ == "__main__":
    solve_system_of_equations()
