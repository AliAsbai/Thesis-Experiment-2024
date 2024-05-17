def can_win(cards):
    suits = {'C', 'D', 'H', 'S'}
    counts = {suit: 0 for suit in suits}

    for card in cards:
        _, suit = card.split()
        counts[suit] += 1

    for suit in suits:
        if counts[suit] >= 2:
            return True

    return False


def main():
    n = int(input().strip())
    if n == 0:
        print("impossible")
        return

    cards = [input().strip() for _ in range(n)]

    if can_win(cards):
        print("possible")
    else:
        print("impossible")


if __name__ == "__main__":
    main()
