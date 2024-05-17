#! /usr/bin/python3

def is_valid_password(stored_password, entered_password):
  """
  Checks if the entered password is valid according to the social media website's rules.

  Args:
      stored_password: The original password stored on the website.
      entered_password: The password the user entered to log in.

  Returns:
      True if the entered password is valid, False otherwise.
  """

  # Case 1: Identical passwords
  if stored_password == entered_password:
    return True

  # Case 2: Check for digit prepend or append with different lengths
  if len(entered_password) == len(stored_password) + 1:
    # Check prepend
    if stored_password.isdigit() and entered_password[0].isdigit() and entered_password[1:] == stored_password:
      return True
    # Check append
    if entered_password[-1].isdigit() and stored_password[-1].isdigit() and entered_password[:-1] == stored_password:
      return True
  return False

  # Case 3: Invalid password length difference (already handled in Case 2)

  # Case 4: Not handled by previous checks (shouldn't occur)
  # return False  # Optional, unreachable code commented out

# Read input
stored_password = input().strip()
entered_password = input().strip()

# Check validity and print result
if is_valid_password(stored_password, entered_password):
  print("Yes")
else:
  print("No")
