def calculate_switch_payout_ratio(percentage):
    # Calculate the total switch points bet on each option
    total_points_option_one = percentage / 100
    total_points_option_two = 1 - total_points_option_one

    # Calculate the switch-payout-ratio for each option
    ratio_option_one = 1 / total_points_option_one
    ratio_option_two = 1 / total_points_option_two

    return ratio_option_one, ratio_option_two

# Read input percentage
percentage = int(input())

# Calculate switch-payout-ratio
ratio_option_one, ratio_option_two = calculate_switch_payout_ratio(percentage)

# Print the results with up to 10 decimal places
print("{:.10f}".format(ratio_option_one))
print("{:.10f}".format(ratio_option_two))
