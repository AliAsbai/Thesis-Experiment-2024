def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def doIntersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
 
    if o1 != o2 and o3 != o4:
        return True
 
    return False

def count_intersections(N):
    if N < 4:
        return 0

    # Number of diagonals = (N * (N - 3)) / 2
    diagonals = (N * (N - 3)) // 2
    intersections = 0

    vertices = [(i, i*i) for i in range(1, N + 1)]  # Example coordinates, you can change as needed

    for i in range(N - 2):
        for j in range(i + 2, N):
            for k in range(i + 1, j):
                for l in range(k + 1, j):
                    if doIntersect(vertices[i], vertices[j], vertices[k], vertices[l]):
                        intersections += 1
    
    return intersections

# Sample input
N = int(input().strip())

# Output the number of intersections
print(count_intersections(N))
