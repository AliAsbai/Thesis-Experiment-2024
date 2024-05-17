import re

def find_patterns(patterns, text):
  """
  Finds all occurrences of patterns in a text, handling empty matches gracefully.

  Args:
      patterns: A list of strings representing patterns to search for.
      text: The string containing the text to search within.

  Returns:
      A list of lists, where each inner list contains the starting positions
      (zero-based indices) of all occurrences of the corresponding pattern
      in the text, or an empty list if no occurrences are found.
  """

  results = []
  for pattern in patterns:
    try:
      # Compile the pattern for efficiency (handle potential invalid patterns)
      compiled_pattern = re.compile(pattern)
    except re.error as e:
      print(f"Invalid pattern: {pattern} ({e})")
      results.append([])  # Append empty list for invalid pattern
      continue

    # Use finditer to get all non-overlapping matches
    matches = compiled_pattern.finditer(text)
    # Extract starting positions or create an empty list if no matches
    results.append([match.start() for match in matches] or [])
  return results

def main():
  """
  Reads input, processes each test case, and prints results.
  """
  while True:
    try:
      # Read number of patterns (handle potential parsing errors)
      try:
        n = int(input())
      except ValueError:
        print("Invalid input. Please enter an integer for the number of patterns.")
        continue

      if n == 0:
        break

      # Read patterns
      patterns = [input() for _ in range(n)]

      # Read text
      text = input()

      # Find occurrences
      results = find_patterns(patterns, text)

      # Print results
      for result in results:
        if result:
          print(" ".join(map(str, result)))  # Print positions if any
        else:
          print("No Match")  # Print "No Match" for empty results

    except EOFError:
      break

if __name__ == "__main__":
  main()
