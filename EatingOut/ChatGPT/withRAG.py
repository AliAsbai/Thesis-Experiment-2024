import sys

for line in sys.stdin:
    m, a, b, c = map(int, line.split())
    if a + b + c > 2 * m:
        print("impossible")
    else:
        print("possible")
