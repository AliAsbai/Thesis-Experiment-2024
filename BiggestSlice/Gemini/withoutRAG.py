import math

def convert_to_radians(degrees, minutes, seconds):
  """Converts degrees, minutes, and seconds to radians."""
  total_seconds = degrees * 60 * 60 + minutes * 60 + seconds
  return math.radians(total_seconds)

def calculate_slice_area(radius, angle):
  """Calculates the area of a single slice."""
  return (1/2) * math.pi * radius**2 * angle

def find_largest_slice(radius, num_slices, angle_degrees, angle_minutes, angle_seconds):
  """Finds the area of the largest slice."""
  # Convert angle to radians
  angle = convert_to_radians(angle_degrees, angle_minutes, angle_seconds)

  # Full circle rotation in radians
  full_rotation = math.pi * 2

  # Special case: Handle non-divisibility of angle and full circle rotation
  if full_rotation % angle != 0:
    # Calculate the largest possible multiple of the original angle within the circle
    largest_multiple = math.floor(full_rotation / angle) * angle
  else:
    # Angle is a divisor of full circle rotation, use the original angle
    largest_multiple = angle

  # Calculate the area of the largest slice using the largest_multiple
  largest_slice_area = calculate_slice_area(radius, largest_multiple)

  # Check if all slices are equal (multiple slices, clean angle division)
  if num_slices > 1 and full_rotation % angle == 0:
    return largest_slice_area
  else:
    # Single slice case (return full pizza area) or unequal slices due to angle
    return calculate_slice_area(radius, full_rotation)

# Read number of test cases
num_tests = int(input())

for _ in range(num_tests):
  # Read test case data
  radius, num_slices = map(int, input().split())
  angle_degrees, angle_minutes, angle_seconds = map(int, input().split())
  
  # Find largest slice area
  largest_area = find_largest_slice(radius, num_slices, angle_degrees, angle_minutes, angle_seconds)
  
  # Print result with formatting for small absolute error tolerance
  print("{:.6f}".format(largest_area))  # Format output to 6 decimal places
