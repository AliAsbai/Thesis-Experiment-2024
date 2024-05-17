def find_R2(R1, S):
    return 2 * S - R1

# Reading input
R1, S = map(int, input().split())

# Finding R2
R2 = find_R2(R1, S)

# Outputting R2
print(R2)
