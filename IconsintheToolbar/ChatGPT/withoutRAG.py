def smallest_toolbar_area(N, sizes):
    sizes.sort()  # Sort the sizes in ascending order
    toolbar_area = 0

    # Calculate the smallest possible area of the toolbar
    for i in range(N):
        toolbar_area += sizes[i] * sizes[2 * N - 1 - i]

    return toolbar_area

# Input
N = int(input())
sizes = []
for _ in range(2 * N):
    sizes.append(int(input()))

# Output
print(smallest_toolbar_area(N, sizes))
