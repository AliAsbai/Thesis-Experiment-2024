def is_valid_password(stored_password, entered_password):
  """
  Checks if the entered password is valid for the stored password based on relaxed validation rules.

  Args:
      stored_password: The password stored for the account (string).
      entered_password: The password entered by the user (string).

  Returns:
      True if the entered password is valid, False otherwise.
  """

  # Check for empty strings (edge case)
  if not stored_password or not entered_password:
    return False  # Empty passwords are not allowed

  # Check if passwords are identical
  if stored_password == entered_password:
    return True

  # Check for prepended/appended digit scenario (improved logic)
  diff_len = len(entered_password) - len(stored_password)
  if abs(diff_len) == 1:  # Only allow one character difference
    if diff_len > 0:  # Prepended digit
      return entered_password[0].isdigit() and entered_password[1:] == stored_password
    else:  # Appended digit
      return entered_password[:-1] == stored_password and entered_password[-1].isdigit()

  # Check for case-reversed version
  reversed_case_password = ''.join([c.lower() if c.isupper() else c.upper() for c in entered_password])
  return reversed_case_password == stored_password

# Read input
stored_password = input()
entered_password = input()

# Check validity and print result
if is_valid_password(stored_password, entered_password):
  print("Yes")
else:
  print("No")
