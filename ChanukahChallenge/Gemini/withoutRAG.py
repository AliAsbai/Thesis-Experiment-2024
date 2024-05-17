def num_candles(days):
  """
  Calculates the total number of candles needed for a Chanukah of 'days' length.

  Args:
      days: An integer representing the number of days for Chanukah.

  Returns:
      An integer representing the total number of candles needed.
  """
  # Calculate the sum of an arithmetic series for regular candles (1 to days)
  regular_candles = days * (days + 1) // 2
  
  # Add the constant number of shammas candles
  shammas_candles = days
  
  # Total candles needed
  total_candles = regular_candles + shammas_candles
  return total_candles

# Read the number of data sets
num_datasets = int(input())

# Loop through each data set
for dataset in range(1, num_datasets + 1):
  # Read the number of days for this data set
  days = int(input().split()[1])
  
  # Calculate and print the number of candles for this data set
  candles = num_candles(days)
  print(f"Dataset {dataset} {candles}")
