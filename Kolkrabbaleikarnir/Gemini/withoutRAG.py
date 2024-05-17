def expected_contestants(n, m):
  """
  Calculates the expected number of contestants remaining after the bridge game.

  Args:
      n: Number of rows in the bridge.
      m: Number of contestants remaining in the game.

  Returns:
      The expected number of contestants remaining after the game.
  """

  # Base cases
  if n == 1:
    return min(m, 1)  # Limit max contestants to 1 at the end
  if m == 1:
    return 0.5  # Only Hlini is playing, 50% chance of passing.

  # Initialize probabilities
  dp = [[0.0] * (m + 1) for _ in range(n + 1)]
  dp[0][1] = 1.0  # Initially all contestants are at the start.

  # Calculate probabilities for each row and number of contestants
  for i in range(1, n + 1):
    for j in range(1, min(m + 1, 2**i)):
      # Probability of contestant passing the current row.
      pass_prob = 0.5

      # Previous contestant's success probability
      if j == 1:  # Only 1 contestant remaining
        prev_pass_prob = 1.0
      elif j == m:  # All spots filled, previous doesn't matter
        prev_pass_prob = dp[i - 1][j - 1]
      else:
        prev_pass_prob = dp[i - 1][j] + dp[i - 1][j - 1]

      # Update probabilities for the current row and contestants.
      dp[i][j] = (prev_pass_prob * pass_prob * (j - 1) +
                  (1 - prev_pass_prob) * pass_prob * j)

      # Handle cases where j exceeds the number of remaining contestants
      if j > m:
        dp[i][j] = 0.0  # No contestant can occupy a non-existent spot

  # Expected number of contestants remaining
  return sum(dp[n])

# Read input
n, m = map(int, input().split())

# Calculate and print expected number of contestants
expected = expected_contestants(n, m)
print(expected)
