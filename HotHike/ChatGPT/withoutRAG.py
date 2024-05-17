def find_best_trip_day(n, temperatures):
    min_max_temp = float('inf')
    best_day = 1

    for start_day in range(n - 2):  # Ensure at least 3 days for the trip
        max_temp = max(temperatures[start_day], temperatures[start_day + 1])
        if max_temp < min_max_temp:
            min_max_temp = max_temp
            best_day = start_day + 1

    return best_day, min_max_temp


# Sample input parsing
n = int(input())
temperatures = list(map(int, input().split()))

# Find the best day for the trip and the resulting maximum temperature during the two hiking days
best_day, max_temperature = find_best_trip_day(n, temperatures)

# Output the result
print(best_day, max_temperature)
