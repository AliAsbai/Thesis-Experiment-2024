import math

def distance_between_boats(boat1, boat2):
  """
  Calculates the Euclidean distance between two boats.

  Args:
      boat1: A tuple containing (x, y) coordinates of the first boat.
      boat2: A tuple containing (x, y) coordinates of the second boat.

  Returns:
      The distance between the boats in meters (rounded to a reasonable precision).
  """
  dx = boat2[0] - boat1[0]
  dy = boat2[1] - boat1[1]
  return round(math.sqrt(dx**2 + dy**2), 6)  # Round to 6 decimal places

def time_to_collision(boat1, boat2, collision_distance,
                       tolerance=1e-6, min_speed_threshold=0.01):
  """
  Calculates the time it takes for two boats to collide, or None if they won't collide.
  Accounts for floating-point errors, very low speeds, and potential division by zero.

  Args:
      boat1: A tuple containing (x, y, direction, speed) of the first boat.
      boat2: A tuple containing (x, y, direction, speed) of the second boat.
      collision_distance: The minimum distance considered a collision (in meters).
      tolerance: A small value to account for floating-point errors (default 1e-6).
      min_speed_threshold: A minimum speed threshold to avoid division by zero (default 0.01).

  Returns:
      The time to collision in seconds (rounded to nearest second), or None if no collision.
  """

  # Calculate relative position and velocity
  dx = boat2[0] - boat1[0]
  dy = boat2[1] - boat1[1]
  dvx = boat2[2] * math.cos(math.radians(boat2[2])) - boat1[2] * math.cos(math.radians(boat1[2]))
  dvy = boat2[2] * math.sin(math.radians(boat2[2])) - boat1[2] * math.sin(math.radians(boat1[2]))

  # Check for parallel courses (no relative movement) or boats already colliding
  if abs(dvx) < tolerance and abs(dvy) < tolerance:
    return None
  if distance_between_boats(boat1, boat2) < collision_distance + tolerance:
    return 0  # Collision imminent

  # Handle very slow speeds (avoid division by zero and inaccurate calculations)
  if abs(dvx) + abs(dvy) < min_speed_threshold:
    # Boats are practically stationary - check if already close enough
    if distance_between_boats(boat1, boat2) < collision_distance:
      return 0  # Consider them colliding
    else:
      return None  # They won't collide

  # Calculate time to meet at closest point (handle potential division by zero)
  try:
    t = (dx * dvy - dy * dvx) / (dvx**2 + dvy**2)
  except ZeroDivisionError:
    # Boats with very similar directions - consider them not colliding
    return None

  # Check if boats will ever meet (negative time means they won't)
  if t < -tolerance:
    return None

  # Return time to collision rounded to nearest second
  return round(t)

def main():
  """
  Reads input and performs collision detection for each test case.
  """
  num_tests = int(input())
  for _ in range(num_tests):
    num_boats, collision_distance = map(float, input().split())
    boats = []
    for _ in range(int(num_boats)):
      boats.append(tuple(map(float, input().split())))

    min_collision_time = float('inf')
    for i in range(len(boats) - 1):
      for j in range(i + 1, len(boats)):
        collision_time = time_to_collision(boats[i], boats[j], collision_distance)
        if collision_time is not None and collision_time < min_collision_time:
          min_collision_time
