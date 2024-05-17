def can_simulate(given_dice, simulated_dice):
    for i in range(3):
        if given_dice[i] == 0:
            if simulated_dice[i] != 0:
                return False
        elif simulated_dice[i] == 0:
            continue
        elif given_dice[i] != 0 and simulated_dice[i] % given_dice[i] != 0:
            return False
    return True

def main():
    test_cases = []
    
    # Read all test cases
    while True:
        given_dice = []
        simulated_dice = []

        for _ in range(4):
            line = input().strip()
            if line == "":
                break
            probabilities = list(map(int, line.split()))
            if probabilities == [0, 0, 0]:
                break
            given_dice.append(probabilities)
        
        if not given_dice:
            break
        
        simulated_dice = given_dice.pop()  # Last set of probabilities is simulated_dice
        test_cases.append((given_dice, simulated_dice))
    
    # Process test cases
    for given_dice, simulated_dice in test_cases:
        result = "YES" if can_simulate(given_dice, simulated_dice) else "NO"
        print(result)

if __name__ == "__main__":
    main()
