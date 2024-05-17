#! /usr/bin/python3

def main():
  # Read input coordinates and battery charge
  start_x, start_y = map(int, input().split())
  end_x, end_y = map(int, input().split())
  battery_charge = int(input())

  # Calculate Manhattan distance (absolute difference in coordinates)
  distance_x = abs(end_x - start_x)
  distance_y = abs(end_y - start_y)
  total_distance = distance_x + distance_y

  # Check if battery is enough
  if total_distance > battery_charge:
    print("N")
  else:
    print("Y")

if __name__ == "__main__":
  main()
