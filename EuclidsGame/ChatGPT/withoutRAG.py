def stan_ollie_game(a, b):
    # Initialize a memoization table
    dp = {}

    # Fill the memoization table bottom-up
    for i in range(1, max(a, b) + 1):
        dp[(i, 0)] = False
        dp[(0, i)] = False

    # Iterate over all possible values from 1 to max(a, b)
    for i in range(1, max(a, b) + 1):
        for j in range(1, max(a, b) + 1):
            # Stan's turn
            stan_wins = False
            for multiple in range(1, max(i, j) // min(i, j) + 1):
                remaining = max(i, j) - min(i, j) * multiple
                if not dp[(min(i, j), remaining)]:
                    stan_wins = True
                    break
            dp[(i, j)] = stan_wins

    return dp[(a, b)]


def main():
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        if stan_ollie_game(a, b):
            print("Stan wins")
        else:
            print("Ollie wins")


if __name__ == "__main__":
    main()
