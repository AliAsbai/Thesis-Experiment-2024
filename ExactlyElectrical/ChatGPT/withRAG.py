import sys

def can_reach_destination(start, destination, charge):
    # Calculate Manhattan distance
    distance = abs(destination[0] - start[0]) + abs(destination[1] - start[1])
    
    # Check if it's possible to reach the destination
    if distance <= charge and (charge - distance) % 2 == 0:
        return "Y"
    else:
        return "N"

if __name__ == "__main__":
    # Read input from STDIN
    for line in sys.stdin:
        # Parse input
        start = tuple(map(int, line.split()))
        destination = tuple(map(int, input().split()))
        charge = int(input())
        
        # Check if it's possible to reach the destination
        result = can_reach_destination(start, destination, charge)
        
        # Print the result
        print(result)
