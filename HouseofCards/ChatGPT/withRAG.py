import sys

for line in sys.stdin:
    h0 = int(line)
    
    # Calculate the smallest h >= h0 such that it is possible to build a tower of height h
    h = h0
    while (((h ^ 2) * 3) + h) // 2 < h0:
        h += 1
    
    print(h)
