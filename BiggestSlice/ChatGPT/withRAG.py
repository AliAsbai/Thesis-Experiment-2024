import sys
import math

def degrees_to_radians(degrees, minutes, seconds):
    return (degrees + minutes / 60 + seconds / 3600) * math.pi / 180

def largest_slice_area(r, n, a_degrees, a_minutes, a_seconds):
    total_angle = degrees_to_radians(a_degrees, a_minutes, a_seconds)
    if total_angle == 2 * math.pi:
        return math.pi * r ** 2  # Special case when rotation covers whole circle
    
    v = [0]
    for i in range(1, n + 1):
        v.append(v[i - 1] + total_angle)
        if v[i] >= 2 * math.pi:
            v[i] -= 2 * math.pi
    
    v.sort()
    
    max_diff = 0
    for i in range(1, n + 1):
        diff = v[i] - v[i - 1]
        max_diff = max(max_diff, diff)

    largest_slice_area = (r ** 2) * math.sin(max_diff / 2)
    return largest_slice_area

if __name__ == "__main__":
    for line in sys.stdin:
        m = int(line)
        for _ in range(m):
            r, n, a_degrees, a_minutes, a_seconds = map(int, input().split())
            result = largest_slice_area(r, n, a_degrees, a_minutes, a_seconds)
            print(result)
