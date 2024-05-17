def max_arithmetic_progression(arr, n, c):
  """
  This function finds the maximum length of an arithmetic progression subsequence
  with length strictly greater than n/c in the given strictly increasing array.

  Args:
      arr: A strictly increasing array of integers.
      n: Length of the array.
      c: Minimum ratio for the subsequence length (must be greater than 1).

  Returns:
      The maximum length of the arithmetic progression subsequence, or -1 if not found.

  Raises:
      ValueError: If the input array is not strictly increasing or if c is less than or equal to 1.
  """

  # Validate input array and minimum ratio (c)
  for i in range(1, n):
    if arr[i] <= arr[i - 1]:
      raise ValueError("Input array is not strictly increasing")
  if c <= 1:
    raise ValueError("Minimum ratio (c) must be greater than 1")

  # Initialize a dictionary to store differences between consecutive elements and
  # their corresponding starting indices.
  differences = {}
  max_length = 0

  for i in range(1, n):
    diff = arr[i] - arr[i - 1]

    # Check if the current difference already exists.
    if diff in differences:
      # Update the max_length only if the current subsequence is valid
      # (length > n/c) and longer than the previous one for this difference.
      current_length = i - differences[diff] + 1
      if current_length > n // c and current_length > max_length:
        max_length = current_length
    else:
      # Add the current difference and its starting index to the dictionary.
      differences[diff] = i

  # Return the maximum length found, or -1 if not found.
  return max_length if max_length > n // c else -1

def main():
  t = int(input())
  for _ in range(t):
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    try:
      result = max_arithmetic_progression(arr, n, c)
      print(result)
    except ValueError as e:
      print(e)

if __name__ == "__main__":
  main()
