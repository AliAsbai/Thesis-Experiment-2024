def play_game(a, b):
  """
  Simulates a game of Stan and Ollie and returns the winner.

  Args:
      a: First positive integer.
      b: Second positive integer.

  Returns:
      "Stan wins" or "Ollie wins" depending on the winner.
  """
  while True:
    # Determine the divisor (smaller number) and handle edge case
    if a >= b:
      divisor = b
      if a < divisor:  # Stan cannot make a move, Ollie wins
        return "Ollie wins"
    else:
      divisor = a
      if b < divisor:  # Ollie cannot make a move, Stan wins
        return "Stan wins"

    # Find the largest valid multiple for subtraction
    multiple = 1
    while a >= divisor * multiple:
      multiple += 1

    # Update the larger number based on the chosen multiple
    a -= divisor * (multiple - 1)

    # Swap a and b for Ollie's turn
    a, b = b, a

    # Check for winner
    if a == 0:
      return "Stan wins"
    if b == 0:
      return "Ollie wins"

# Read input
while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break

  # Simulate and print the winner
  winner = play_game(a, b)
  print(winner)
