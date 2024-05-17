import math

def calculate_area(radius, angle):
  """
  Calculates the area of a circle sector.

  Args:
      radius: The radius of the circle in centimeters.
      angle: The angle of the sector in degrees.

  Returns:
      The area of the sector in square centimeters.
  """
  return (angle / 360) * math.pi * radius**2

def solve_test_case(radius, num_slices, angle_deg, angle_min, angle_sec):
  """
  Solves a single test case for the largest pizza slice area.

  Args:
      radius: The radius of the pizza in centimeters.
      angle_deg: The degrees of the rotation angle.
      angle_min: The minutes of the rotation angle.
      angle_sec: The seconds of the rotation angle.

  Returns:
      The area of the largest slice in square centimeters.
  """
  # Convert angle to degrees
  total_angle = angle_deg + angle_min / 60 + angle_sec / 3600

  # Track cutting positions, considering wrapping around the circle
  cutting_positions = [0]
  current_angle = 0
  for _ in range(num_slices):
    current_angle += total_angle
    current_angle = current_angle % 360  # Ensure angle stays within 0-360
    cutting_positions.append(current_angle)

  # Find biggest gap considering wrapping around the circle
  largest_gap = 0
  for i in range(1, len(cutting_positions)):
    gap = (cutting_positions[i] - cutting_positions[i-1]) % 360
    largest_gap = max(largest_gap, gap)

  # Calculate and print area of largest slice
  largest_slice_area = calculate_area(radius, largest_gap)
  print(largest_slice_area)

# Read number of test cases
num_test_cases = int(input())

# Solve each test case
for _ in range(num_test_cases):
  radius, num_slices, angle_deg, angle_min, angle_sec = map(int, input().split())
  solve_test_case(radius, num_slices, angle_deg, angle_min, angle_sec)
