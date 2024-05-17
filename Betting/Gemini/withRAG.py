#! /usr/bin/python3

def calculate_payout_ratio(percentage):
  """
  Calculates the switch-payout-ratio for an option based on its percentage of total bets.

  Args:
      percentage: The percentage of total bets for the option (0 < percentage < 100).

  Returns:
      A tuple containing the switch-payout-ratio for the option and its complementary option.
  """
  # Calculate payout ratio for option 1
  ratio_option_1 = 100.0 / percentage

  # Calculate payout ratio for option 2 (complementary)
  ratio_option_2 = 100.0 / (100 - percentage)

  return ratio_option_1, ratio_option_2

# Read input
for line in sys.stdin:
  percentage = int(line)

  # Calculate payout ratios
  ratio_option_1, ratio_option_2 = calculate_payout_ratio(percentage)

  # Print results with at most 3 decimal places
  print(f"{ratio_option_1:.3f}")
  print(f"{ratio_option_2:.3f}")
