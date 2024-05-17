import sys

def find_best_location(points):
    # Calculate centroid
    centroid_x = sum(point[0] for point in points) / len(points)
    centroid_y = sum(point[1] for point in points) / len(points)

    # Round centroid to nearest grid point
    best_x = round(centroid_x)
    best_y = round(centroid_y)

    return (best_x, best_y)

for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    
    best_location = find_best_location(points)
    print(best_location[0], best_location[1])
