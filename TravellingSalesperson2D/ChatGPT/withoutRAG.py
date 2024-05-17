import math

def euclidean_distance(point1, point2):
    return round(math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2))

def greedy_tour(N, points):
    tour = [0]
    used = [False] * N
    used[0] = True
    for i in range(1, N):
        best = -1
        for j in range(N):
            if not used[j] and (best == -1 or euclidean_distance(points[tour[i-1]], points[j]) < euclidean_distance(points[tour[i-1]], points[best])):
                best = j
        tour.append(best)
        used[best] = True
    return tour

# Read input
N = int(input())
points = []
for _ in range(N):
    x, y = map(float, input().split())
    points.append((x, y))

# Solve TSP using GreedyTour algorithm
tour = greedy_tour(N, points)

# Output the tour
for node in tour:
    print(node)
