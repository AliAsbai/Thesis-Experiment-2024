import sys

def solve():
  """Reads input, checks for possibility, and finds a word if possible."""
  # Read input
  line = sys.stdin.readline().strip().split()
  length = int(line[0])
  weight = int(line[1])

  # Check if word formation is possible
  if weight / length > 26 or weight / length < 1:
    print("impossible")
    return

  # Build the word by iteratively trying different character combinations
  for first_char_weight in range(1, 27):  # Iterate through starting character weights
    remaining_weight = weight - first_char_weight
    remaining_length = length - 1
    word = chr(ord('a') + first_char_weight - 1)

    # Recursively check if a word can be formed with remaining weight and length
    if find_word(remaining_weight, remaining_length, word):
      return  # Found a solution, exit

def find_word(remaining_weight, remaining_length, word):
  """Recursive function to build the remaining word based on weight and length."""
  if remaining_length == 0 and remaining_weight == 0:
    print(word)
    return True  # Word found

  if remaining_length <= 0 or remaining_weight < 0:
    return False  # Not possible to form a word

  for char_weight in range(1, 27):
    if remaining_weight - char_weight >= 0:
      new_word = word + chr(ord('a') + char_weight - 1)
      if find_word(remaining_weight - char_weight, remaining_length - 1, new_word):
        return True  # Found a solution within the recursion

  return False  # No solution found in this branch

if __name__ == "__main__":
  solve()
