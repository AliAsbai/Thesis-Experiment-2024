def determine_quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4

# Read input
x = int(input())
y = int(input())

# Determine quadrant
quadrant = determine_quadrant(x, y)

# Output result
print(quadrant)
