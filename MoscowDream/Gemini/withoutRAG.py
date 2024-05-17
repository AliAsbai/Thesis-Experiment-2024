def is_possible_problemset(easy, medium, hard, total):
  """
  This function checks if it's possible to create a problemset with the given constraints.

  Args:
      easy: Number of easy problems (0 <= easy <= 10).
      medium: Number of medium problems (0 <= medium <= 10).
      hard: Number of hard problems (0 <= hard <= 10).
      total: Total number of problems desired (1 <= total <= 20).

  Returns:
      "YES" if a valid problemset can be created, "NO" otherwise.
  """

  # Validate input to ensure it meets the specified ranges.
  if not (0 <= easy <= 10 and 0 <= medium <= 10 and 0 <= hard <= 10 and 1 <= total <= 20):
    return "Invalid Input: Please enter values within the specified ranges."

  # Check if at least one problem of each difficulty exists.
  if easy == 0 or medium == 0 or hard == 0:
    return "NO"

  # Check if there are enough problems to meet the total requirement.
  if easy + medium + hard < total:
    return "NO"

  # Since at least one of each type exists and total requirement is met, a valid problemset can be created.
  return "YES"

# Get input from the user in a loop to handle potential invalid input.
while True:
  try:
    easy, medium, hard, total = map(int, input().split())
    break  # Exit the loop if input is valid
  except ValueError:
    print("Invalid Input: Please enter integers separated by spaces.")

# Call the function and print the result.
print(is_possible_problemset(easy, medium, hard, total))
