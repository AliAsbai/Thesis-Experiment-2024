from collections import Counter

def is_multigram(word):
  """
  Checks if the given word is a multigram and returns the shortest root.

  Args:
      word: A string containing lowercase English characters.

  Returns:
      The shortest root of the multigram if it is one, otherwise -1.
  """
  char_count = Counter(word)
  min_root_len = len(word)
  root = None
  
  for sublen in range(1, len(word) // 2 + 1):
    # Check if the word is divisible by the sub-string length
    if len(word) % sublen != 0:
      continue
    
    # Check if all characters can be divided equally into substrings
    current_count = char_count.copy()
    valid = True
    for i in range(0, len(word), sublen):
      if current_count != Counter(word[i:i+sublen]):
        valid = False
        break
      for char, count in Counter(word[i:i+sublen]).items():
        current_count[char] -= count
    if valid:
      min_root_len = sublen
      root = word[:sublen]
      break  # No need to check further lengths if a valid root is found

  return root if root else -1

# Read input word
word = input()

# Check for multigram and print result
root = is_multigram(word)
print(root)
