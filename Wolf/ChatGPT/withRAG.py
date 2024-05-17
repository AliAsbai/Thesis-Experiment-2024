import sys

def can_win(n, cards):
    if n > 26:
        return True

    suits = {'C': set(), 'D': set(), 'H': set(), 'S': set()}
    max_rank = 0

    for card in cards:
        rank, suit = card.split()
        rank = int(rank)
        max_rank = max(max_rank, rank)
        suits[suit].add(rank)

    opponent_has_highest = all(len(suit) > 0 for suit in suits.values())
    opponent_highest = max(max(suit) for suit in suits.values()) if opponent_has_highest else 0

    return opponent_has_highest and opponent_highest < max_rank

def main():
    for line in sys.stdin:
        data = line.strip().split()
        if len(data) == 1:
            n = int(data[0])
            if n == 0:
                print("impossible")
            else:
                cards = [input().strip() for _ in range(n)]
                if can_win(n, cards):
                    print("possible")
                else:
                    print("impossible")

if __name__ == "__main__":
    main()
