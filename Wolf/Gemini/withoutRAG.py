from collections import deque

def is_possible(hand):
  """
  Checks if it's possible to win the game by reshuffling the hand.

  Args:
      hand: A list of cards represented as tuples (rank, suit).

  Returns:
      "possible" if it's possible to win, "impossible" otherwise.
  """
  # Convert hand to deques for efficient manipulation
  player_hand = deque(hand)
  opponent_hand = deque([None] * (52 - len(hand)))

  # Check if any card in the opponent's hand can guarantee a win
  for card in player_hand:
    if all(opponent_hand[0][0] > card[0] and suit == card[1] for suit in ['C', 'D', 'H', 'S'] if opponent_hand[0] and opponent_hand[0][1] == suit):
      return "impossible"

  # Track seen suits and corresponding highest ranks encountered (excluding opponent's first card)
  seen_suits = set()
  highest_ranks = {'C': None, 'D': None, 'H': None, 'S': None}

  for _ in range(len(hand)):
    player_card = player_hand.popleft()
    seen_suits.add(player_card[1])

    # Check if opponent has a higher card for the same suit, excluding the first card
    opponent_card = opponent_hand.popleft()
    if opponent_card and opponent_card[0] > player_card[0] and opponent_card[1] == player_card[1] and len(opponent_hand) > 0:  # Check if opponent has remaining cards of the same suit
      return "impossible"

    # Update highest ranks for seen suits (excluding opponent's first card)
    highest_ranks[player_card[1]] = max(highest_ranks.get(player_card[1]), player_card[0])

    # Check if all suits have been seen and a win is guaranteed
    if len(seen_suits) == 4 and all(highest_rank is None or player_card[0] > highest_rank for player_card in player_hand):
      return "possible"

    opponent_hand.append(player_card)

  # No guaranteed win or loss found
  return "impossible"

# Read input
num_cards = int(input())
hand = []
for _ in range(num_cards):
  rank, suit = map(str, input().split())
  hand.append((int(rank), suit))

# Print output
print(is_possible(hand))
