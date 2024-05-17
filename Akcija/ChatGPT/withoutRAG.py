def minimal_price(N, prices):
    prices.sort(reverse=True)  # Sort the prices in descending order
    total_price = 0
    i = 0

    while i < N:
        # If there are 2 or more books remaining
        if i + 2 < N:
            total_price += prices[i] + prices[i + 1]  # Add the prices of two most expensive books
            i += 3  # Move to the next group of books
        else:
            total_price += prices[i]  # Add the price of the remaining book
            i += 1

    return total_price

# Reading input
N = int(input())
prices = []
for _ in range(N):
    prices.append(int(input()))

# Outputting the minimal price
print(minimal_price(N, prices))
