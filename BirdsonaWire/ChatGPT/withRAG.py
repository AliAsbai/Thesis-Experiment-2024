import sys

def additional_birds(l, d, n, positions):
    if n == 0:
        # If there are no birds on the wire, calculate the maximum number of birds
        # that can be placed based on the distance from the poles and the spacing required.
        return (l - 12) // d + 1
    
    additional = 0
    
    # Check the distance between each bird and the next one
    for i in range(n - 1):
        gap = positions[i + 1] - positions[i]
        additional += max(0, (gap - d) // d)
    
    # Check the space between the first bird and the beginning of the wire
    additional += max(0, (positions[0] - 6) // d)
    
    # Check the space between the last bird and the end of the wire
    additional += max(0, (l - 6 - positions[-1]) // d)
    
    return additional

if __name__ == "__main__":
    for line in sys.stdin:
        l, d, n = map(int, line.split())
        positions = [int(input()) for _ in range(n)]
        positions.sort()  # Sort the positions
        result = additional_birds(l, d, n, positions)
        print(result)
