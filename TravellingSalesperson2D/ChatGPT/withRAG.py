import sys
import math

def euclidean_distance(point1, point2):
    return round(math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2))

def greedy_tour(n, points):
    tour = [0]
    used = [False] * n
    used[0] = True
    
    for i in range(1, n):
        best = -1
        for j in range(n):
            if not used[j] and (best == -1 or euclidean_distance(points[tour[i-1]], points[j]) < euclidean_distance(points[tour[i-1]], points[best])):
                best = j
        tour.append(best)
        used[best] = True
    
    return tour

# Read input
for line in sys.stdin:
    n = int(line)
    points = []
    for _ in range(n):
        x, y = map(float, input().split())
        points.append((x, y))
    
    # Calculate GreedyTour
    tour = greedy_tour(n, points)
    
    # Print tour
    for city in tour:
        print(city)
