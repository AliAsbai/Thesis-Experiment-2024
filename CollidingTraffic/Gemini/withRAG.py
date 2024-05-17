#! /usr/bin/python3

import math


def time_to_collision(boat1, boat2, collision_distance):
  """
  Calculates the time to collision between two boats.

  Args:
      boat1: A tuple containing (x1, y1, direction1, speed1).
      boat2: A tuple containing (x2, y2, direction2, speed2).
      collision_distance: The minimum distance considered a collision.

  Returns:
      The time to collision in seconds, or None if they won't collide.
  """
  dx = boat2[0] - boat1[0]
  dy = boat2[1] - boat1[1]
  initial_distance = math.sqrt(dx**2 + dy**2)

  # Check if boats are not moving towards each other or already on top of each other
  if (dx * (math.cos(math.radians(boat1[2])) - math.cos(math.radians(boat2[2]))) + 
      dy * (math.sin(math.radians(boat1[2])) - math.sin(math.radians(boat2[2])))) <= 0 or initial_distance <= collision_distance:
    return None

  # Check if boats are moving directly towards each other (avoid division by zero)
  if abs(math.cos(math.radians(boat1[2])) - math.cos(math.radians(boat2[2]))) < 1e-6 and \
     abs(math.sin(math.radians(boat1[2])) - math.sin(math.radians(boat2[2]))) < 1e-6:
    return 0  # Instant collision

  # Alternative approach - calculate time based on initial distance and speed of one boat
  time_to_collision = initial_distance / (boat1[3] if boat2[3] == 0 else boat2[3])
  return time_to_collision if time_to_collision > 0 else None


def main():
  """
  Reads input, processes each test case, and prints results.
  """
  for line in sys.stdin:
    num_boats, collision_distance = map(float, line.split())

    boats = []
    for _ in range(int(num_boats)):
      boat_data = list(map(float, sys.stdin.readline().split()))
      boats.append(boat_data)

    # Find the earliest collision time
    earliest_collision = float('inf')
    for i in range(len(boats)):
      for j in range(i + 1, len(boats)):
        collision_time = time_to_collision(boats[i], boats[j], collision_distance)
        if collision_time is not None and collision_time < earliest_collision:
          earliest_collision = collision_time

    if earliest_collision == float('inf'):
      print("No collision.")
    else:
      print(int(math.ceil(earliest_collision)))


if __name__ == "__main__":
  main()
