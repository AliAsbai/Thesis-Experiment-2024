# Function to rearrange integers based on the desired order
def rearrange_integers(A, B, C, order):
    # Sort the integers
    integers = sorted([A, B, C])
    
    # Rearrange the integers based on the order
    rearranged_integers = [0, 0, 0]
    for i, char in enumerate(order):
        if char == 'A':
            rearranged_integers[i] = integers[0]
        elif char == 'B':
            rearranged_integers[i] = integers[1]
        elif char == 'C':
            rearranged_integers[i] = integers[2]
    
    # Return the rearranged integers as a string
    return ' '.join(map(str, rearranged_integers))

# Read input
A, B, C = map(int, input().split())
order = input().strip()

# Rearrange integers and print the result
print(rearrange_integers(A, B, C, order))
