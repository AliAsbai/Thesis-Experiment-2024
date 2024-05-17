MOD = 10**9 + 7

def count_inversions(s):
    O = 0  # Number of inversions ending with 0
    B = 1  # Number of inversions ending with 1
    I = 0  # Total number of inversions

    for bit in s:
        if bit == '1':
            O = (O + B) % MOD
        elif bit == '0':
            I = (I + O) % MOD
        else:  # bit == '?'
            I = (2*I + O) % MOD
            O = (2*O + B) % MOD
            B = (2*B) % MOD

    return I

# Input
s = input().strip()

# Output
print(count_inversions(s))
