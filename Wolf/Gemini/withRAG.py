#! /usr/bin/python3

from collections import Counter

def is_possible(my_cards):
  """
  Checks if it's possible to win the Wolf game by reshuffling the cards.

  Args:
      my_cards: A list of cards represented as tuples (rank, suit).

  Returns:
      "possible" if it's possible to win, "impossible" otherwise.
  """
  num_cards = len(my_cards)
  if num_cards > 26:
    return "possible"  # More cards than opponent's minimum, guaranteed win

  # Track highest card for each suit and total value per suit
  highest_values = {'C': 0, 'D': 0, 'H': 0, 'S': 0}
  total_values = {'C': 0, 'D': 0, 'H': 0, 'S': 0}

  # Iterate through cards and update values
  for rank, suit in my_cards:
    highest_values[suit] = max(highest_values[suit], rank)
    total_values[suit] += rank

  # Check if any suit has significantly fewer cards
  card_counts = Counter(suit for _, suit in my_cards)
  for suit, count in card_counts.items():
    if count < num_cards / 4 - 2:
      return "impossible"  # Too few cards in a suit, can't win

  # Check potential winning scenarios based on highest card and total value distributions
  winning_scenarios = 0
  
  # Scenario 1: Highest card in each suit can win a round (excluding ties)
  if len(set(highest_values.values())) == len(highest_values):
    winning_scenarios += 1

  # Scenario 2: Total value in a suit can win multiple rounds if highest card is tied
  for suit, total in total_values.items():
    if total > sum(highest_values.values()) - highest_values[suit]:
      winning_scenarios += 1
      
  # If at least one winning scenario exists, return "possible"
  if winning_scenarios > 0:
    return "possible"

  return "impossible"

# Read input from STDIN
my_cards = []
for line in sys.stdin:
  rank, suit = map(int, line.strip().split())
  my_cards.append((rank, suit))

# Print the result
print(is_possible(my_cards))
