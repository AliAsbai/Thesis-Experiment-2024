def calculate_other_endpoint(x1, y1):
    # Center of the pool
    center_x = 250 / 2
    center_y = 250 / 2

    # Find the distance between the given endpoint and the center of the pool
    dist_x = center_x - x1
    dist_y = center_y - y1

    # Calculate the coordinates of the other endpoint
    other_x = center_x + dist_y
    other_y = center_y - dist_x

    return other_x, other_y

# Input
x1, y1 = map(int, input().split())

# Calculate the other endpoint
other_x, other_y = calculate_other_endpoint(x1, y1)

# Output the result rounded to two decimal digits
print("{:.2f} {:.2f}".format(other_x, other_y))
