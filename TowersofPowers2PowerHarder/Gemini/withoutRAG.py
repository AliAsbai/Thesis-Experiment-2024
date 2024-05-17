def tower_of_powers(base, exponents):
  """
  Calculates the value of a tower of powers representation.

  Args:
      base: A list of base numbers (after removing leading zeros).
      exponents: A list of exponents for each base.

  Returns:
      The integer value of the tower of powers representation.
  """
  result = 1
  for b, e in zip(base, exponents):
    if b == 0:
      raise ValueError("Base cannot be zero")
    result *= b**e
  return result

def sort_towers(towers):
  """
  Sorts a list of towers of powers representations, preserving
  original order for duplicates using a custom sorting key.

  Args:
      towers: A list of strings representing towers of powers.

  Returns:
      A list of strings representing the sorted towers of powers,
      preserving original order for duplicates.
  """

  def key_func(tower):
    """
    Key function for sorting towers based on value and potentially
    additional criteria (modify as needed).

    Args:
        tower: String representing a tower of powers.

    Returns:
        A tuple (value, original_index) for stable sorting and
        potential additional sorting criteria.
    """
    base, exponents = [int(x) for x in tower.split("^")[:-1]], [int(x) for x in tower.split("^")[1:]]
    value = tower_of_powers(base, exponents)
    original_index = towers.index(tower)
    # Add additional sorting criteria here if needed (e.g., prioritize specific bases)
    return (value, original_index)

  sorted_towers = sorted(towers, key=key_func)
  return sorted_towers

def main():
  """
  Reads input, sorts towers, and prints the output.
  """
  num_towers = int(input())
  towers = []

  for _ in range(num_towers):
    tower = input()
    # Remove leading zeros from bases before processing
    tower = tower.lstrip("0")
    if not tower.count("^") == len(tower.split("^")) - 2:
      raise ValueError("Invalid input format")
    towers.append(tower)

  sorted_towers = sort_towers(towers)
  print("Case 1:")
  for tower in sorted_towers:
    print(tower)

if __name__ == "__main__":
  main()
