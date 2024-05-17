#! /usr/bin/python3

def game(a, b):
  """
  This function determines the winner for a given starting state (a, b).

  Args:
      a: The smaller number.
      b: The larger number.

  Returns:
      True if Stan wins, False if Ollie wins.
  """
  # Ensure b is always larger
  if b < a:
    a, b = b, a

  # Iterative approach to replace deep recursion
  while True:
    # Base cases: When B is a multiple of A or 1 less than A
    if b % a == 0:
      return True  # Stan wins (B is a multiple of A)
    elif b == a - 1:
      return False  # Ollie wins (B is 1 less than A)

    # Reduce B by multiples of A until it leaves a remainder of 1
    remainder = b % a
    b -= remainder

    # Check if remaining B is 0 (Ollie wins) or 1 (refer to base case)
    if b == 0:
      return False
    elif b == 1:
      return not game(a, remainder)  # Recursive call for the last step

# Read input until encountering "0 0"
while True:
  line = input().strip().split()
  if line == ["0", "0"]:
    break
  a, b = map(int, line)

  # Determine winner based on the game function
  winner = "Stan wins" if game(a, b) else "Ollie wins"

  # Print the winner for the current game
  print(winner)
