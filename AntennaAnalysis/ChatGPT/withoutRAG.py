def find_most_significant_difference(n, c, measurements):
    max_diff = 0
    max_diff_index = 0
    result = []

    for i in range(n):
        current_measurement = measurements[i]

        # Find the maximum difference between current_measurement and any earlier measurement
        current_max_diff = 0
        for j in range(max_diff_index, i):
            diff = abs(current_measurement - measurements[j]) - c * abs(i - j)
            if diff > current_max_diff:
                current_max_diff = diff

        # Update max_diff if necessary
        if current_max_diff > max_diff:
            max_diff = current_max_diff
            max_diff_index = i

        result.append(max(0, max_diff))

    return result

# Input
n, c = map(int, input().split())
measurements = list(map(int, input().split()))

# Output
result = find_most_significant_difference(n, c, measurements)
print(*result)
