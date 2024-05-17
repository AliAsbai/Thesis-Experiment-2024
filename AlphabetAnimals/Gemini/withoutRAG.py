def can_survive(last_word, unused_words):
  """
  Analyzes whether a valid move exists to survive or eliminate the next player.

  Args:
      last_word: The preceding animal name in the game.
      unused_words: A list of remaining unused animal names.

  Returns:
      The optimal strategy as a string:
          - A word starting with the last letter of `last_word` (eliminates next player).
          - Any unused word with a distinct first letter (survival if no elimination).
          - "?" if no valid move is available (even for survival).
  """

  last_letter = last_word[-1]

  # Prioritize finding a word to eliminate the next player
  for word in unused_words:
    if word[0] == last_letter and word != last_word:
      return word + "!"  # Eliminate

  # Check for any word with a distinct first letter for survival
  seen_letters = set(last_word)  # Track encountered letters to avoid duplicates
  for word in unused_words:
    if word[0] == last_letter and word not in seen_letters:
      return word  # Survive (distinct first letter)
    seen_letters.add(word[0])  # Keep track of seen letters

  # No valid move found (edge case: all unused words start with last letter and are duplicates)
  return "?"

# Input handling
last_word = input()
n = int(input())
unused_words = [input() for _ in range(n)]

# Determine and print the optimal move
move = can_survive(last_word, unused_words)
print(move)
