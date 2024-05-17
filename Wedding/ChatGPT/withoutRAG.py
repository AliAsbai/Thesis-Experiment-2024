def find_seating_arrangement(n, m, pairs):
    def is_valid(seating, pairs):
        for pair in pairs:
            husband, wife = pair.split()
            husband = int(husband[:-1])
            wife = int(wife[:-1])
            if (husband in seating and wife in seating):
                return False
        return True

    def backtrack(seating, index):
        if index == n:
            if is_valid(seating, pairs):
                return seating
            return None

        seating[index] = 0
        result = backtrack(seating, index + 1)
        if result:
            return result

        seating[index] = 1
        result = backtrack(seating, index + 1)
        if result:
            return result

        return None

    seating = [-1] * n
    seating[0] = 0  # Bride sits on one side, groom on the other
    result = backtrack(seating, 1)
    if result:
        return ' '.join([str(i) + ('h' if result[i] == 1 else 'w') for i in range(1, n)])
    return "bad luck"

# Sample input
test_cases = [
    (10, 6, ["3h 7h", "5w 3w", "7h 6w", "8w 3w", "7h 3w", "2w 5h"])
]

# Process each test case
for n, m, pairs in test_cases:
    result = find_seating_arrangement(n, m, pairs)
    print(result)
