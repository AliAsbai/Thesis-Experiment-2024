import sys

def distance(a1, b1, a2, b2):
  """Calculates the Manhattan distance between two points."""
  return abs(a1 - a2) + abs(b1 - b2)

def can_reach_on_time(cab_location, next_ride_departure, source, travel_time):
  """Checks if the cab can reach the source address before next ride's departure."""
  next_departure_hour, next_departure_minute = map(int, next_ride_departure.split(":"))
  current_hour, current_minute = map(int, cab_location.split(":"))
  travel_minutes = travel_time + (next_departure_hour - current_hour) * 60 + (next_departure_minute - current_minute)
  return travel_minutes >= 0

def schedule_rides(rides):
  """Schedules rides using a greedy approach."""
  cabs = 1
  current_cab = rides[0]  # Entire tuple (departure_time, source_x, source_y, dest_x, dest_y)
  for i in range(1, len(rides)):
    departure_time, source_x, source_y, dest_x, dest_y = rides[i]
    travel_time = distance(source_x, source_y, current_cab[1], current_cab[2])
    if not can_reach_on_time(current_cab[0], departure_time, source_y + ":" + source_x, travel_time):
      cabs += 1
      current_cab = (departure_time, dest_x, dest_y)
    else:
      current_cab = (departure_time, dest_x, dest_y)
  return cabs

for line in sys.stdin:
  num_scenarios = int(line)
  for _ in range(num_scenarios):
    num_rides = int(sys.stdin.readline())
    rides = []
    for _ in range(num_rides):
      departure_time, source_x, source_y, dest_x, dest_y = sys.stdin.readline().strip().split()
      rides.append((departure_time, int(source_x), int(source_y), int(dest_x), int(dest_y)))
    min_cabs = schedule_rides(rides)
    print(min_cabs)
