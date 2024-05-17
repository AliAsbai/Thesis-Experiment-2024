from heapq import heappush, heappop

def calculate_travel_time(source, destination):
  """Calculates travel time between two addresses."""
  return abs(source[0] - destination[0]) + abs(source[1] - destination[1])

def handle_midnight_rides(taxis, ride, rides):
  """Checks if a taxi can complete subsequent rides after a midnight ride."""
  for next_ride in rides[rides.index(ride) + 1:]:
    # Calculate travel time considering midnight
    travel_time = calculate_travel_time(taxis[0], next_ride[1:3])
    # Check if taxi can reach next ride on time or complete midnight rides
    if next_ride[0] >= taxis[0] + travel_time:
      heappop(taxis)  # Free taxi if it can complete future rides
      return True
  return False

def schedule_taxis(rides):
  """Schedules taxi rides and returns the minimum number of taxis needed."""
  taxis = []  # Min-heap to store available taxis (departure time)
  heappush(taxis, rides[0][0])  # Add first ride's departure time

  for ride in rides[1:]:
    # Check if current taxi can reach the new ride on time
    if ride[0] >= taxis[0] + calculate_travel_time(taxis[0], ride[1:3]):
      heappop(taxis)  # Free taxi if it can reach new ride on time
    elif handle_midnight_rides(taxis, ride, rides):
      # Taxi can complete subsequent rides after a midnight ride
      continue  # Don't assign current ride to this taxi
    heappush(taxis, ride[0])  # Add new ride's departure time

  return len(taxis)

def main():
  """Reads input, solves each scenario, and prints the results."""
  num_scenarios = int(input())
  for _ in range(num_scenarios):
    num_rides = int(input())
    rides = []
    for _ in range(num_rides):
      departure_time, source_x, source_y, destination_x, destination_y = input().split()
      rides.append((int(departure_time[:2]), int(departure_time[3:]), (int(source_x), int(source_y)), (int(destination_x), int(destination_y))))
    rides.sort()  # Sort rides by departure time

    min_taxis = schedule_taxis(rides)
    print(min_taxis)

if __name__ == "__main__":
  main()
