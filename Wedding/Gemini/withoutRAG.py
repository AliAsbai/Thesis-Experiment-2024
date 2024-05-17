import random

def seating_arrangement(couples, affairs, attempts=10000):
  """
  This function finds a seating arrangement for a wedding feast using simulation.

  Args:
      couples: Number of couples attending the feast (1 <= couples <= 30).
      affairs: Number of adulterous pairs (0 <= affairs <= 50).
      affairs_list: List of tuples representing the adulterous pairs 
                    (husband_id, wife_id).
      attempts: Number of random seating attempts (default 10000).

  Returns:
      A list of guests (excluding bride and groom) on the bride's side 
      or "bad luck" if no solution is found after attempts.
  """
  # Initialize variables
  n = couples * 2  # Total number of guests
  guest_list = [i for i in range(1, n)]  # List of guests (excluding bride & groom)
  affairs_list = [(int(pair.split()[0]), int(pair.split()[1])) for pair in affairs]

  # Function to check if seating a couple together creates a bad situation
  def check_affair(guest1, guest2):
    for affair in affairs_list:
      if (guest1 in affair and guest2 in affair) or (guest1 == guest2):
        return True
    return False

  # Simulation loop
  for _ in range(attempts):
    random.shuffle(guest_list)  # Randomize guest order
    seating = []
    # Prioritize placing guests with no affairs or fewest affairs first
    guest_affair_count = {guest: 0 for guest in guest_list}
    for affair in affairs_list:
      for guest in affair:
        guest_affair_count[guest] += 1
    sorted_guests = sorted(guest_list, key=lambda x: guest_affair_count[x])

    for guest in sorted_guests:
      found = False
      for other_guest in seating:
        if not check_affair(guest, other_guest):
          seating.append(guest)
          found = True
          break
      if found:
        break  # Stop searching once a guest is placed

    if len(seating) == len(guest_list):
      return seating

  return "bad luck"

# Read input from user or file (modify as needed)
couples = int(input("Enter the number of couples: "))
affairs = int(input("Enter the number of adulterous pairs: "))
affair_descriptions = [input("Enter affair details (husband couple_id wife couple_id): ") for _ in range(affairs)]

# Find seating arrangement
seating_plan = seating_arrangement(couples, affair_descriptions)

# Print output
if seating_plan == "bad luck":
  print(seating_plan)
else:
  print(f"Guests on bride's side: {seating_plan}")
