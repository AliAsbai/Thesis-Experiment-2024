import sys

for line in sys.stdin:
    x = int(line)
    y = int(next(sys.stdin))
    
    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    else:
        print(4)
