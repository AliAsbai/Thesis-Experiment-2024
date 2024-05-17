import sys

def can_create_problemset(a, b, c, n):
    # Check if there are enough problems of each difficulty level
    if a == 0 or b == 0 or c == 0 or a + b + c < n or n < 3:
        return "NO"
    else:
        return "YES"

if __name__ == "__main__":
    for line in sys.stdin:
        a, b, c, n = map(int, line.split())
        print(can_create_problemset(a, b, c, n))
