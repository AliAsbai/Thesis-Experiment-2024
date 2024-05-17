def is_acceptable(S, P):
    # Condition 1: P and S are identical
    if P == S:
        return True
    
    # Condition 2: S can be formed from P by prepending a single digit (0–9)
    for digit in range(10):
        if str(digit) + P == S:
            return True
    
    # Condition 3: S can be formed from P by appending a single digit (0–9)
    for digit in range(10):
        if P + str(digit) == S:
            return True
    
    # Condition 4: S is equal to P after reversing the case of all letters in P
    if P.swapcase() == S:
        return True
    
    return False

# Input
S = input().strip()
P = input().strip()

# Output
if is_acceptable(S, P):
    print("Yes")
else:
    print("No")
