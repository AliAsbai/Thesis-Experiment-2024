def main():
    # Input: number of contestants (N) and number of huffle-puff problems (P)
    N, P = map(int, input().split())

    # Initialize total carrots count
    total_carrots = 0

    # Loop through each contestant
    for _ in range(N):
        # Read contestant description
        contestant_description = input()
        
        # Check if the contestant solved any huffle-puff problems
        if 'huffle-puff' in contestant_description:
            # Increment total carrots count
            total_carrots += P

    # Output total number of carrots
    print(total_carrots)

if __name__ == "__main__":
    main()
