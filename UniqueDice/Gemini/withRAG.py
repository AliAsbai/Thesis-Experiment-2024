#! /usr/bin/python3

from collections import Counter

def find_largest_set(dice):
  """
  Finds the size of the largest set of identical dice in the collection.

  Args:
      dice: A list of lists, where each inner list represents the faces of a die.

  Returns:
      The size of the largest set of identical dice.
  """
  # Store all possible rotations (including 180-degree flips) as strings.
  rotations = set()
  for die in dice:
    for _ in range(3):  # Consider three rotations (0, 120, and 180 degrees)
      rotations.add(tuple(die))
      die.reverse()  # Reverse the die for 180-degree flip
      rotations.add(tuple(die))
      die.append(die.pop(0))  # Rotate clockwise for other orientations

  # Count the occurrences of each unique die rotation.
  counts = Counter(rotations)
  
  # Return the size of the most frequent die rotation.
  return max(counts.values(), default=0)

def main():
  """
  Reads input, calls the function to find the largest set, and prints the result.
  """
  n = int(input())
  dice = []
  for _ in range(n):
    dice.append(list(map(int, input().split())))
  
  largest_set = find_largest_set(dice)
  print(largest_set)

if __name__ == "__main__":
  main()
