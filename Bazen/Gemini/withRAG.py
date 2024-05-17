#! /usr/bin/python3

def main():
  """
  Calculates the other endpoint of the dividing line segment.
  """
  x1, y1 = map(int, input().split())

  # Special case: both coordinates are zero (origin)
  if x1 == 0 and y1 == 0:
    x2, y2 = 125, 125
  else:
    # Calculate slope
    slope = (y1 - 125) / (x1 - 250)  # Corrected slope calculation

    # Calculate x-coordinate of second endpoint (intersection with x-axis)
    x2 = 0  # Since the line intersects the x-axis

    # Calculate y-coordinate of second endpoint
    y2 = slope * (x2 - x1) + y1

  # Round coordinates to two decimal places
  print(f"{x2:.2f} {y2:.2f}")

if __name__ == "__main__":
  main()
