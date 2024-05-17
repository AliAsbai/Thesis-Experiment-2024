def find_number(m, n, p, q):
    for i in range(10**(m - n - 1), 10**(m - n)):
        remaining_digits = str(i)
        original_number = int(remaining_digits + str(p))
        new_number = original_number * q
        if len(str(new_number)) == m and str(new_number)[:(m - n)] == remaining_digits:
            return new_number
    return "IMPOSSIBLE"

# Sample input parsing
m, n, p, q = map(int, input().split())

# Call the function and print the result
print(find_number(m, n, p, q))
