#! /usr/bin/python3

def additional_birds(l, d, n, positions):
  """
  Calculates the maximum number of additional birds that can sit on the wire.

  Args:
      l: Length of the wire in centimeters.
      d: Minimum distance between birds in centimeters.
      n: Number of birds already sitting on the wire.
      positions: List of positions of the birds on the wire.

  Returns:
      The maximum number of additional birds that can sit on the wire.
  """
  # Sort the positions of the birds (only if there are birds)
  if n > 0:
    positions.sort()

  # Case 1: Check space between birds
  additional_birds = 0
  for i in range(n - 1):
    distance = positions[i + 1] - positions[i]
    additional_birds += (distance - d) // (d - 1)

  # Case 2: Check space before first bird (handle case with no birds)
  additional_birds += (l - 6) // d

  # Case 3: Check space after last bird (handle case with no birds)
  additional_birds += (l - 6) // d

  return additional_birds

if __name__ == "__main__":
  # Read input
  l, d, n = map(int, input().split())
  positions = []
  for _ in range(n):
    positions.append(int(input()))

  # Calculate and print result
  result = additional_birds(l, d, n, positions)
  print(result)
