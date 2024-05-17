def simulate_battle(godzilla_army, mechagodzilla_army):
  """
  Simulates a battle between Godzilla and MechaGodzilla's armies.

  Args:
      godzilla_army: A list of integers representing the strengths of Godzilla's monsters.
      mechagodzilla_army: A list of integers representing the strengths of MechaGodzilla's monsters.

  Returns:
      A string indicating the winner ("Godzilla", "MechaGodzilla", or "uncertain").
  """

  while godzilla_army and mechagodzilla_army:
    # Find the minimum strengths in each army
    godzilla_weakest = min(godzilla_army)
    mechagodzilla_weakest = min(mechagodzilla_army)

    # Remove the weakest monster(s) efficiently using list comprehension
    godzilla_army = [strength for strength in godzilla_army if strength > godzilla_weakest]
    mechagodzilla_army = [strength for strength in mechagodzilla_army if strength > mechagodzilla_weakest]

  # Check who won based on remaining monsters
  if godzilla_army:
    return "Godzilla"
  elif mechagodzilla_army:
    return "MechaGodzilla"
  else:
    return "uncertain"

def main():
  """
  Reads input, simulates battles, and prints the outcome for each test case.
  """
  try:
    num_test_cases = int(input())
  except ValueError:
    print("Invalid input: Please enter a valid number of test cases.")
    return

  for _ in range(num_tset_cases):
    try:
      # Read the number of monsters in each army with error handling
      godzilla_army_size, mechagodzilla_army_size = map(int, input().split())
      if godzilla_army_size <= 0 or mechagodzilla_army_size <= 0:
        print("Invalid input: Army size must be positive.")
        continue

      # Read the strengths of Godzilla's monsters with error handling
      godzilla_army = list(map(int, input().split()))
      if any(strength <= 0 for strength in godzilla_army):
        print("Invalid input: Monster strength must be positive.")
        continue

      # Read the strengths of MechaGodzilla's monsters with error handling
      mechagodzilla_army = list(map(int, input().split()))
      if any(strength <= 0 for strength in mechagodzilla_army):
        print("Invalid input: Monster strength must be positive.")
        continue

      # Simulate the battle and print the winner
      winner = simulate_battle(godzilla_army, mechagodzilla_army)
      print(winner)
    except ValueError:
      print("Invalid input: Please enter valid integers for army size and monster strengths.")

if __name__ == "__main__":
  main()
