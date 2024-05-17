def switch_payout_ratio(percentage_option_one):
  """
  This function calculates the switch-payout-ratio for each option
  in a switch bet.

  Args:
      percentage_option_one (int): Percentage of total bets for option one (0 < a < 100).

  Returns:
      tuple: A tuple containing the switch-payout-ratio for option one and option two.
  """
  # Calculate percentage for option two
  percentage_option_two = 100 - percentage_option_one

  # Convert percentages to decimals
  decimal_option_one = percentage_option_one / 100
  decimal_option_two = percentage_option_two / 100

  # Calculate payout ratio for option one (1 / (percentage of option two))
  payout_ratio_option_one = 1 / decimal_option_two

  # Calculate payout ratio for option two (1 / (percentage of option one))
  payout_ratio_option_two = 1 / decimal_option_one

  return payout_ratio_option_one, payout_ratio_option_two

# Get user input
percentage_option_one = int(input("Enter percentage of bets for option one (0-99): "))

# Ensure valid input
if not 0 < percentage_option_one < 100:
  print("Invalid input: Please enter a number between 0 and 99.")
  exit()

# Calculate and print payout ratios
payout_ratio_one, payout_ratio_two = switch_payout_ratio(percentage_option_one)

print(f"Switch-payout-ratio for option one: {payout_ratio_one:.10f}")
print(f"Switch-payout-ratio for option two: {payout_ratio_two:.10f}")
