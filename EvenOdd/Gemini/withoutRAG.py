MODULO = 10**9 + 7


def solve(L, R):
    # Initialize variables for efficient calculations
    count_even, count_odd = 0, 0
    prev_even, prev_odd = 0, 0

    # Iterate from L to R
    for x in range(L, R + 1):
        # Update counts based on parity
        if x % 2 == 0:
            count_even = (prev_even + count_odd) % MODULO
        else:
            count_odd = (prev_even + count_odd) % MODULO

        # Update previous values for next iteration
        prev_even = count_even
        prev_odd = count_odd

    # Calculate final sum with handling for edge cases
    if L % 2 == 0:
        result = count_even
    else:
        result = (count_even + count_odd) % MODULO

    return result


# Read input
L, R = map(int, input().split())

# Solve and print the result
result = solve(L, R)
print(result)
