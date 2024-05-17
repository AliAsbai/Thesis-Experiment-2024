def reverse_binary(N):
    # Convert integer N to binary string and remove '0b' prefix
    binary_str = bin(N)[2:]
    
    # Reverse the binary string
    reversed_binary_str = binary_str[::-1]
    
    # Convert the reversed binary string back to integer
    reversed_binary_int = int(reversed_binary_str, 2)
    
    return reversed_binary_int

# Input
N = int(input().strip())

# Output
print(reverse_binary(N))
