from collections import defaultdict

def min_essay_length(words, synonyms):
  """
  Calculates the minimum number of characters in the essay with shortest synonyms.

  Args:
      words: List of words in the essay.
      synonyms: List of word pairs representing synonyms.

  Returns:
      The minimum number of characters excluding spaces.
  """

  # Build a dictionary to efficiently map words to their shortest synonyms
  word_map = defaultdict(str)

  def find_root(word):
    """
    Recursively finds the root of a word in the synonym tree,
    performing path compression for efficiency.
    """
    if word not in word_map:
      word_map[word] = word  # Initialize as itself if no synonym found
    if word_map[word] != word:
      # Path compression: Directly update to the root on subsequent lookups
      word_map[word] = find_root(word_map[word])
    return word_map[word]

  # Process synonyms to build the synonym tree
  for a, b in synonyms:
    root_a = find_root(a)
    root_b = find_root(b)
    # Update the root of the synonym with the shorter word
    if len(root_a) > len(root_b):
      word_map[root_a] = root_b

  # Calculate the total length of shortest synonyms
  total_length = 0
  for word in words:
    # Use the original word if no synonym found
    root = word_map.get(word, word)
    total_length += len(root)
  return total_length

# Read input
n, m = map(int, input().split())
words = input().split()
synonyms = [input().split() for _ in range(m)]

# Calculate and print the minimum length
print(min_essay_length(words, synonyms))
