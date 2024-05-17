import sys

def max_guests(R, C, apartment):
    guests = 0

    # Convert the first row of the apartment into integers
    first_row = [1 if char == '.' else 0 for char in apartment[0]]

    # Iterate through the rest of the apartment
    for i in range(1, R):
        row = [0] * C
        for j in range(C):
            if apartment[i][j] == '.':
                # If it's a free space, assign the value of the position
                # 1 column over plus 1
                row[j] = first_row[j] + 1
            else:
                # If it's blocked, reset the value to 0
                row[j] = 0

        # Now iterate over all possible table heights
        for h in range(1, 1001):
            length = 0
            for j in range(C):
                if row[j] >= h:
                    length += 1
                    # Calculate the maximum number of guests
                    guests = max(guests, 2 * (length + h))
                else:
                    length = 0

        # Update first_row for the next iteration
        first_row = row

    return guests - 1

if __name__ == "__main__":
    for line in sys.stdin:
        R, C = map(int, line.split())
        if R == 0 and C == 0:
            break  # Exit loop if no more input
        apartment = [input() for _ in range(R)]
        print(max_guests(R, C, apartment))
