def min_days_for_statues(n):
  """
  This function calculates the minimum number of days needed to print at least n statues
  with a single 3D printer that can also print new printers.

  Args:
      n: The number of statues needed.

  Returns:
      The minimum number of days needed.
  """
  # Initialize with 1 printer and 0 days
  printers = 1
  days = 0

  # Loop until we have enough statues printed
  while printers < n:
    # Option 1: Print statues with all printers
    statues_printed = min(n - printers, printers)  # Print only what's needed
    days += 1
    printers += statues_printed  # Update printers based on statues printed

  return days

# Get user input
n = int(input("Enter the number of statues needed: "))

# Call the function and print the result
days = min_days_for_statues(n)
print(f"Minimum days needed to print {n} statues: {days}")
