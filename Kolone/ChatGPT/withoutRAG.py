def swap_ants(ants1, ants2):
    """
    Function to simulate swapping of ants between two rows.
    """
    new_ants1 = list(ants1)
    new_ants2 = list(ants2)
    for i in range(len(ants1)):
        # If ants are facing opposite directions and can swap, swap them
        if (ants1[i][1] == 'R' and ants2[i][1] == 'L'):
            new_ants1[i], new_ants2[i] = new_ants2[i], new_ants1[i]
    return new_ants1, new_ants2

def ant_order_after_seconds(N1, N2, ants1, ants2, T):
    """
    Function to find the order of ants after T seconds.
    """
    for _ in range(T):
        ants1, ants2 = swap_ants(ants1, ants2)
    combined_ants = ants1 + ants2
    return ''.join([ant[0] for ant in combined_ants])

# Sample Input Parsing
N1, N2 = map(int, input().split())
ants1 = input().strip()
ants2 = input().strip()
T = int(input().strip())

# Convert ants to a list of tuples containing ant and its direction
ants1 = [(ants1[i], 'L') for i in range(N1)]
ants2 = [(ants2[i], 'R') for i in range(N2)]

# Find order of ants after T seconds
result = ant_order_after_seconds(N1, N2, ants1, ants2, T)
print(result)
