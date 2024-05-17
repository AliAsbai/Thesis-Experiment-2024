#! /usr/bin/python3

def check_seating(seating, couples, affairs):
  """
  Checks if a seating arrangement avoids bad luck scenarios.

  Args:
      seating: A list representing the seating on the bride's side.
      couples: A dictionary mapping couple number to (husband, wife).
      affairs: A list of tuples representing adulterous pairs.

  Returns:
      True if the seating is valid, False otherwise.
  """
  for husband, wife in affairs:
    # Check if either member of the affair is already seated
    if husband in seating or wife in seating:
      return False
  return True

def backtrack(seating, couples, affairs, n, current_guest):
  """
  Solves the seating arrangement using backtracking with duplicate and affair handling.

  Args:
      seating: A list representing the current seating on the bride's side.
      couples: A dictionary mapping couple number to (husband, wife).
      affairs: A list of tuples representing adulterous pairs.
      n: Number of couples.
      current_guest: Index of the guest to be seated (1 to n-1).

  Returns:
      True if a valid seating arrangement is found, False otherwise.
  """
  # Base case: All guests seated on bride's side
  if current_guest == n:
    return True

  # Try seating current guest on the bride's side (avoid duplicates and affairs)
  if couples[current_guest][0] not in seating:
    # Check if anyone from guest's affairs (excluding partner) is already seated
    if not any(person in seating for person in (couples[idx][0] for idx in 
                [affair[0] for affair in affairs if current_guest in affair and affair[0] != couples[current_guest][1]])):
      seating.append(couples[current_guest][0])
      if check_seating(seating, couples, affairs):
        # Recursively try seating remaining guests
        if backtrack(seating, couples, affairs, n, current_guest + 1):
          return True
        # Backtrack if no valid seating found with current guest on bride's side
        seating.pop()

  # Implicitly try seating current guest on the groom's side (by moving on)
  if backtrack(seating, couples, affairs, n, current_guest + 1):
    return True

  # No valid seating found with current guest on either side
  return False

def solve(n, m, couples, affairs):
  """
  Calls the backtracking function to find a valid seating arrangement.

  Args:
      n: Number of couples.
      m: Number of adulterous pairs.
      couples: A dictionary mapping couple number to (husband, wife).
      affairs: A list of tuples representing adulterous pairs.

  Returns:
      A list representing the seating on the bride's side if a solution exists,
      "bad luck" otherwise.
  """
  seating = []
  if backtrack(seating, couples, affairs, n-1, 1):
    return seating
  return "bad luck"

def main():
  """
  Reads input and calls the solver function.
  """
  for line in sys.stdin:
    n, m = map(int, line.split())
    couples = {i: (str(i) + "h", str(i) + "w") for i in range(n)}
    affairs = []
    for _ in range(m):
      affairs.append(tuple(line.split()))
    seating = solve(n-1, m, couples, affairs)
    print(*seating)

if __name__ == "__main__":
  main()
