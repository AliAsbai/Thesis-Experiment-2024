import sys

def count_intersections(N):
    if N < 4:
        return 0

    intersections = 0
    for i in range(1, N - 2 + 1):
        for j in range(N - 2 - i, 0, -1):
            intersections += i * j

    return intersections

if __name__ == "__main__":
    for line in sys.stdin:
        N = int(line)
        intersections = count_intersections(N)
        print(intersections)
