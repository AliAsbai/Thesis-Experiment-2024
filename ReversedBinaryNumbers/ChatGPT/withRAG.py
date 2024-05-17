import sys

for line in sys.stdin:
    N = int(line.strip())
    X = 0
    while N != 0:
        X = (X << 1) | (N & 1)
        N >>= 1
    print(X)
