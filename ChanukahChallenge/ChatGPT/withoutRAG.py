# Function to calculate the total number of candles needed for an N-day Chanukah holiday
def calculate_candles_needed(days):
    total_candles = 0
    for day in range(1, days + 1):
        total_candles += day + 1  # Add the number of candles for the day plus the shammas candle
    return total_candles

# Main function to process input and output
def main():
    # Read the number of data sets
    num_data_sets = int(input().strip())

    # Process each data set
    for i in range(num_data_sets):
        # Read the data set number and the number of days
        data_set_number, days = map(int, input().strip().split())

        # Calculate the number of candles needed for the given number of days
        candles_needed = calculate_candles_needed(days)

        # Output the result
        print(data_set_number, candles_needed)

# Run the main function
if __name__ == "__main__":
    main()
