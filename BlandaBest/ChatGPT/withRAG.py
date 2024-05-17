import sys

# Read input
meat_types = [input().strip() for _ in range(int(input().strip()))]

# Determine output
if len(meat_types) == 1:
    print(meat_types[0])
else:
    if "nautakjot" in meat_types and "kjuklingur" in meat_types:
        print("blandad best")
    elif "nautakjot" in meat_types:
        print("nautakjot")
    elif "kjuklingur" in meat_types:
        print("kjuklingur")
