from collections import Counter

def largest_dice_set(dice):
  """
  Finds the size of the largest set of identical dice in a collection,
  handling cases where dice might have repeated faces.

  Args:
      dice: A list of lists, where each inner list represents a single die
          with its six face values (unordered).

  Returns:
      The size of the largest set of identical dice.
  """

  # Create a dictionary to store counts for each distinct face value pattern
  face_counts = Counter()

  # Iterate through each die
  for die in dice:
    # Create a tuple to represent the unique face value pattern
    # This ensures correct grouping even with repeated face values
    pattern = tuple(sorted(Counter(die).values()))
    face_counts[pattern] += 1

  # Find the maximum count (size of the largest set)
  return max(face_counts.values(), default=0)

# Read the number of dice
n = int(input())

# Read the dice faces
dice = []
for _ in range(n):
  dice.append(list(map(int, input().split())))

# Find and print the largest set size
largest_set = largest_dice_set(dice)
print(largest_set)
