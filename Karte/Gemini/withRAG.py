#! /usr/bin/python3

suits = ["P", "K", "H", "T"]

def check_deck(card_labels):
  """
  Checks if a deck of cards is complete and returns the number of missing cards for each suit.

  Args:
      card_labels: String containing all card labels separated by no separators.

  Returns:
      A list containing the number of missing cards for each suit (P, K, H, T).
  """
  seen_cards = {suit: [False] * 13 for suit in suits}
  for label in card_labels:
    suit, rank = label[0], int(label[1:])
    if seen_cards[suit][rank - 1]:
      return ["GRESKA"]  # Duplicate card found
    seen_cards[suit][rank - 1] = True
  return [13 - sum(cards) for cards in seen_cards.values()]

# Read input string
card_labels = input().strip()

# Check deck and print output
missing_cards = check_deck(card_labels)
if missing_cards == ["GRESKA"]:
  print("GRESKA")
else:
  print(" ".join(map(str, missing_cards)))
