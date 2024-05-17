import sys

def min_shelves_needed(small, medium, big, shelf_width):
    # Calculate the total width occupied by each type of book
    total_width = small + 2*medium + 3*big
    
    # Calculate the number of shelves needed based on total width and shelf width
    shelves_needed = total_width // shelf_width
    if total_width % shelf_width != 0:
        shelves_needed += 1
    
    return shelves_needed

# Read input
for line in sys.stdin:
    small, medium, big = map(int, line.split())
    shelf_width = int(input())

    # Calculate the minimum number of shelves needed
    min_shelves = float('inf')
    for s in range(small + 1):
        for m in range(medium + 1):
            for b in range(big + 1):
                total_width = s + 2*m + 3*b
                shelves_needed = total_width // shelf_width
                if total_width % shelf_width != 0:
                    shelves_needed += 1
                min_shelves = min(min_shelves, shelves_needed)
    
    print(min_shelves)
