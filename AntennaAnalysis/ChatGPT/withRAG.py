import sys

def calculate_max_difference(n, c, measurements):
    # Initialize arrays to store intermediate results
    max_diff = [0] * n
    max_so_far = float('-inf')
    
    # Iterate over measurements
    for i in range(n):
        # Calculate the current day's maximum difference
        max_diff[i] = max(0, max_so_far + measurements[i] - c * i)
        
        # Update max_so_far for the next iteration
        max_so_far = max(max_so_far, measurements[i] + c * i)
    
    return max_diff

if __name__ == "__main__":
    for line in sys.stdin:
        n, c = map(int, line.split())
        measurements = list(map(int, sys.stdin.readline().split()))
        
        result = calculate_max_difference(n, c, measurements)
        print(*result)
