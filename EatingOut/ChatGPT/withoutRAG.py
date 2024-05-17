def is_possible(m, a, b, c):
    # Check if the total number of items picked by all three is greater than or equal to the total number of unique items available
    if (a + b + c) >= m:
        return "impossible"
    else:
        return "possible"

# Reading input
m, a, b, c = map(int, input().split())

# Checking possibility and printing output
print(is_possible(m, a, b, c))
