import sys
 
for line in sys.stdin:
    R1, S = map(int, line.split())
    R2 = 2 * S - R1
    print(R2)
