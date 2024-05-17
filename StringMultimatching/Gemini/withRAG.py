#! /usr/bin/python3

def search_pattern(text, pattern):
  """Searches for all occurrences of a pattern in text using brute force with optimizations."""
  n = len(text)
  m = len(pattern)
  occurrences = []
  
  # Iterate through the text
  for i in range(n - m + 1):
    # Check if pattern matches at current position
    if text[i:i + m] == pattern:
      occurrences.append(i)
      # Optimized early exit if no further matches are possible
      if i + m == n:
        break
      
  return occurrences

for line in sys.stdin:
  # Read number of patterns
  n = int(line)

  # Read patterns
  patterns = [line.strip() for _ in range(n)]

  # Read text
  text = sys.stdin.readline().strip()

  # Search for each pattern
  for pattern in patterns:
    occurrences = search_pattern(text, pattern)
    if occurrences:
      print(*occurrences)
    else:
      print()
