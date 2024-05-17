def can_create_problemset(a, b, c, n):
    # Check if there are enough problems of each difficulty level
    if a >= 1 and b >= 1 and c >= 1:
        # Check if total number of problems is at least 3
        if n >= 3:
            return "YES"
    return "NO"

# Sample input reading
a, b, c, n = map(int, input().split())

# Check if it is possible to create the problemset
result = can_create_problemset(a, b, c, n)
print(result)
