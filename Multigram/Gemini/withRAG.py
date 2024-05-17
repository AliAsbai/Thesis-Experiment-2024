#! /usr/bin/python3

from collections import Counter

def is_anagram(word1, word2):
  """
  Checks if two words are anagrams.
  """
  return Counter(word1) == Counter(word2)

def find_multigram_root(word):
  """
  Finds the shortest root if the word is a multigram, otherwise returns -1.
  """
  word_len = len(word)
  if word_len < 2:
    return -1

  # Find all factors of the word length (excluding 1)
  factors = [i for i in range(2, word_len + 1) if word_len % i == 0]

  # Iterate through factors in ascending order
  for factor in factors:
    # Split the word into substrings of size 'factor'
    substrings = [word[i:i+factor] for i in range(0, word_len, factor)]
    
    # Check if all substrings are anagrams
    if all(is_anagram(substrings[0], substring) for substring in substrings[1:]):
      return substrings[0]

  return -1

# Read input word
word = input().strip()

# Find and print the multigram root
root = find_multigram_root(word)
print(root)
