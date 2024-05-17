#! /usr/bin/python3

def battle(godzilla_strengths, mechagodzilla_strengths):
  """
  Simulates the battle between Godzilla and MechaGodzilla's armies.

  Args:
      godzilla_strengths: A sorted list of strengths of Godzilla's monsters.
      mechagodzilla_strengths: A sorted list of strengths of MechaGodzilla's monsters.

  Returns:
      A string indicating the winner: "Godzilla", "MechaGodzilla", or "uncertain".
  """

  while godzilla_strengths and mechagodzilla_strengths:
    # Compare the weakest monsters of each army
    godzilla_weakest = godzilla_strengths[0]
    mechagodzilla_weakest = mechagodzilla_strengths[0]

    if godzilla_weakest < mechagodzilla_weakest:
      # Godzilla's army is stronger
      del godzilla_strengths[0]
    elif godzilla_weakest > mechagodzilla_weakest:
      # MechaGodzilla's army is stronger
      del mechagodzilla_strengths[0]
    else:
      # Both armies have equally weak monsters
      # Randomly remove one from MechaGodzilla's army (following the problem rule)
      del mechagodzilla_strengths[0]

  # Winner is the army with remaining monsters
  if godzilla_strengths:
    return "Godzilla"
  elif mechagodzilla_strengths:
    return "MechaGodzilla"
  else:
    return "uncertain"

def main():
  """
  Reads input, simulates battles, and prints the outcome for each test case.
  """
  # Read the number of test cases
  test_cases = int(input())

  for _ in range(test_cases):
    # Skip a blank line
    input()

    # Read the number of monsters in each army
    godzilla_monsters, mechagodzilla_monsters = map(int, input().split())

    # Read the strengths of Godzilla's monsters
    godzilla_strengths = sorted(map(int, input().split()))

    # Read the strengths of MechaGodzilla's monsters
    mechagodzilla_strengths = sorted(map(int, input().split()))

    # Simulate the battle and print the winner
    winner = battle(godzilla_strengths, mechagodzilla_strengths)
    print(winner)

if __name__ == "__main__":
  main()
