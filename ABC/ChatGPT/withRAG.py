import sys

# Function to rearrange numbers based on desired order
def rearrange_numbers(order, A, B, C):
    if order == 'ABC':
        return A, B, C
    elif order == 'ACB':
        return A, C, B
    elif order == 'BAC':
        return B, A, C
    elif order == 'BCA':
        return B, C, A
    elif order == 'CAB':
        return C, A, B
    elif order == 'CBA':
        return C, B, A

# Reading input from stdin
for line in sys.stdin:
    # Splitting the line into numbers and order
    numbers = list(map(int, line.strip().split()))
    order = input().strip()
    
    # Sorting numbers
    A, B, C = sorted(numbers)
    
    # Rearranging numbers based on desired order
    result = rearrange_numbers(order, A, B, C)
    
    # Printing the result
    print(*result)
