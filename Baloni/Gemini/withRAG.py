#! /usr/bin/python3

def main():
  # Read the number of balloons
  num_balloons = int(input())

  # Initialize a list to store balloon counts at each height
  balloon_heights = [0] * 1000001

  # Read balloon heights and update the count list
  for height in map(int, input().split()):
    balloon_heights[height] += 1

  # Initialize variables for tracking arrows and current height
  arrows = 0
  current_height = max(balloon_heights)

  # Loop through balloon heights in descending order
  for height in range(current_height, -1, -1):
    # Pop balloons at current height (if any)
    if balloon_heights[height] > 0:
      arrows += 1
      balloon_heights[height] -= 1

    # Check and handle balloons above (if any)
    if height > 0 and balloon_heights[height - 1] > 0:
      balloon_heights[height - 1] -= 1
      # Update current_height only if there are NO balloons at current height after handling above
      if balloon_heights[height] == 0:
        current_height = height - 1

  # Print the minimum number of arrows
  print(arrows)

if __name__ == "__main__":
  main()
