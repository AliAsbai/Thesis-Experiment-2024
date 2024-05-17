import sys

for line in sys.stdin:
    data = line.strip()
    if '1' in data:
        print('1')
    else:
        print('0')
