def expected_contestants(n, m):
    # Base case: if there are no contestants or no rows in the bridge, return the number of contestants
    if n == 0 or m == 0:
        return m

    # Initialize a list to store the probabilities of each number of contestants remaining
    prob_remaining = [0] * (m + 1)
    prob_remaining[m] = 1  # Initially, all contestants are there

    # Iterate over each row of the bridge
    for _ in range(n):
        # Initialize a temporary list to store updated probabilities
        temp_prob = [0] * (m + 1)

        # Update probabilities for each possible remaining contestant count after crossing this row
        for remaining in range(m + 1):
            # Probability that a contestant survives this row
            prob_survive = remaining / m

            # Update probabilities for all possible remaining contestant counts after crossing this row
            temp_prob[remaining] += prob_remaining[remaining] * prob_survive
            temp_prob[remaining - 1] += prob_remaining[remaining] * (1 - prob_survive)

        # Update prob_remaining for the next row
        prob_remaining = temp_prob

    # Calculate expected number of contestants remaining after crossing all rows
    expected = sum(i * prob_remaining[i] for i in range(m + 1))
    return expected

# Reading input
n, m = map(int, input().split())

# Calculate and print the expected number of contestants
print(expected_contestants(n, m))
