import sys

def count_missing_cards(deck):
    suits = {'P': [False] * 13, 'K': [False] * 13, 'H': [False] * 13, 'T': [False] * 13}
    
    for i in range(0, len(deck), 3):
        card = deck[i:i+3]
        suit = card[0]
        rank = int(card[1:])
        
        if suits[suit][rank-1]:
            return "GRESKA"
        else:
            suits[suit][rank-1] = True
    
    missing_counts = [13 - sum(suit) for suit in suits.values()]
    return ' '.join(map(str, missing_counts))

if __name__ == "__main__":
    for line in sys.stdin:
        deck = line.strip()
        result = count_missing_cards(deck)
        print(result)
