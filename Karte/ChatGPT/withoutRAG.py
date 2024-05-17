def count_missing_cards(deck):
    # Dictionary to count occurrences of each card label
    card_count = {'P': 0, 'K': 0, 'H': 0, 'T': 0}

    # List to store encountered card labels for duplicate check
    encountered_cards = []

    # Loop through the deck string and process each card label
    for i in range(0, len(deck), 3):
        card = deck[i:i+3]
        suit = card[0]
        number = int(card[1:])
        
        # Check for duplicates
        if card in encountered_cards:
            return "GRESKA"
        else:
            encountered_cards.append(card)

        # Increment count for the respective suit
        card_count[suit] += 1

    # Calculate missing cards for each suit
    missing_cards = [13 - count for count in card_count.values()]

    return ' '.join(map(str, missing_cards))


# Main function
if __name__ == "__main__":
    # Input
    deck = input().strip()
    
    # Output
    print(count_missing_cards(deck))
