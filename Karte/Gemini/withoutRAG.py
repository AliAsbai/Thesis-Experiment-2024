def check_deck(deck_string):
  """
  This function checks if a deck of poker cards is complete and returns the missing cards for each suit.

  Args:
      deck_string: A string containing all the card labels (e.g., P01K02H03).

  Returns:
      A string "GRESKA" if there's a duplicate card, otherwise a string with four space-separated numbers indicating missing cards for each suit (P, K, H, T).
  """

  # Initialize counters for each suit and a set to store seen cards.
  suit_counts = {'P': 0, 'K': 0, 'H': 0, 'T': 0}
  seen_cards = set()

  # Loop through each card label.
  for card in deck_string:
    suit = card[0]
    rank = int(card[1:])

    # Check for valid rank (1-13).
    if rank not in range(1, 14):
      return "GRESKA"

    # Check for duplicate card.
    if (suit, rank) in seen_cards:
      return "GRESKA"

    # Update counters based on suit.
    suit_counts[suit] += 1

    # Add card to seen cards set.
    seen_cards.add((suit, rank))

  # Calculate missing cards for each suit.
  missing_cards = [str(13 - count) for count in suit_counts.values()]

  return " ".join(missing_cards)

# Read input string
deck_string = input()

# Call the function and print the result
result = check_deck(deck_string)
print(result)
