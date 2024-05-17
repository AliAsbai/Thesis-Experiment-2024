#! /usr/bin/python3

def gcd(a, b):
  """
  Calculates the greatest common divisor of two integers.
  """
  while b:
    a, b = b, a % b
  return a

def is_feasible(dice, target):
  """
  Checks if the target die outcome can be simulated using the given dice.

  Args:
      dice: A list of 3 lists, where each inner list represents the probabilities
          (integers) of rolling 1, 2, and 3 for a specific die.
      target: A list of 3 integers representing the probabilities of rolling 1, 2,
          and 3 for the desired die.

  Returns:
      True if the target outcome can be simulated, False otherwise.
  """
  # Calculate the greatest common divisor (GCD) of all target probabilities.
  target_gcd = gcd(target[0], gcd(target[1], target[2]))

  # Check if any target outcome probability is 0.
  if target_gcd == 0:
    return False

  # Check if it's possible to achieve each target outcome probability
  # by using a combination of the dice.
  for i in range(3):
    # Check if target outcome only has one possible value (probability 10000).
    if target[i] == target_gcd:
      found = False
      for die in dice:
        # Check if die can only roll the same value as target.
        if die[i] == target_gcd and sum(die) == target_gcd:
          found = True
          break
      if not found:
        return False
      continue  # Skip further checking for this outcome

    # Scale probabilities by GCD to avoid floating-point errors.
    scaled_target = target[i] // target_gcd
    for die in dice:
      scaled_die = die[i] // target_gcd
      if scaled_die > 0 and (scaled_target % scaled_die == 0 or scaled_die > scaled_target):
        found = True
        break
    if not found:
      return False
  return True

for line in sys.stdin:
  if line.strip() == "0 0 0":
    break
  dice = []
  for _ in range(3):
    dice.append([int(x) for x in line.strip().split()])
  target = [int(x) for x in sys.stdin.readline().strip().split()]
  print("YES" if is_feasible(dice, target) else "NO")
