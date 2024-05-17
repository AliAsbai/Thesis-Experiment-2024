from collections import defaultdict

def weight_of_word(word):
  """Calculates the weight of a word by summing letter weights (a=1, ..., z=26)"""
  return sum(ord(char) - ord('a') + 1 for char in word)

def find_word(length, weight, alphabet="abcdefghijklmnopqrstuvwxyz"):
  """
  Finds a word of given length and weight using a backtracking approach with optimizations.

  Args:
      length: The desired length of the word.
      weight: The desired weight of the word.
      alphabet: String containing the allowed lowercase letters (default is a-z).

  Returns:
      A string of length 'length' with weight 'weight' if found, otherwise "impossible".
  """

  # Use a dictionary to store possible starting characters and their remaining weights
  possible_starts = defaultdict(list)

  # Iterate through alphabet, prioritizing high-weight characters but handling edge cases
  for char in sorted(alphabet, reverse=True):
    remaining_weight = weight - (ord(char) - ord('a') + 1)
    # Check if remaining weight can be achieved (avoid negative values)
    if remaining_weight >= 0:
      possible_starts[remaining_weight].append(char)
    # If remaining weight is 0 and length is 1, return the character (base case)
    elif remaining_weight == 0 and length == 1:
      return char

  # Recursively explore possible starting characters
  for remaining_weight, starting_chars in possible_starts.items():
    for char in starting_chars:
      result = find_word(length - 1, remaining_weight, alphabet)
      if result != "impossible":
        return char + result

  return "impossible"

# Read input
length, weight = map(int, input().split())

# Find the word or determine impossibility
result = find_word(length, weight)

# Print the output
print(result)
