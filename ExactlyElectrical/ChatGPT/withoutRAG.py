def can_reach_destination(start, end, charge):
    start_x, start_y = start
    end_x, end_y = end
    
    # Calculate the Manhattan distance between start and end points
    distance = abs(start_x - end_x) + abs(start_y - end_y)
    
    # Check if the charge is enough to cover the distance
    if distance <= charge and (charge - distance) % 2 == 0:
        return "Y"
    else:
        return "N"

# Reading input
start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))
charge = int(input())

# Checking if destination can be reached
result = can_reach_destination(start, end, charge)
print(result)
