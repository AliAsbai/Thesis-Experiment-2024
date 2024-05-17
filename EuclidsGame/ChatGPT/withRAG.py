import sys

def game(A, B):
    # Step 1: Check if B is greater than A, if not, swap them
    if B < A:
        A, B = B, A
    
    # Step 2: Check for winning conditions
    if B % A == 0:
        return True
    elif B // A == 1:
        return not game(A, B - A)
    else:
        return True

for line in sys.stdin:
    A, B = map(int, line.split())
    if A == 0 and B == 0:
        break
    
    if game(A, B):
        print("Stan wins")
    else:
        print("Ollie wins")
