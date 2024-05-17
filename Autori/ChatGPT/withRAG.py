import sys
 
for line in sys.stdin:
    names = line.strip().split('-')
    short_variation = ''.join(name[0].upper() for name in names)
    print(short_variation)
