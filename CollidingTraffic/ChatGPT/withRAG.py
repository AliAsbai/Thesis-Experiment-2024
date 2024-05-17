import sys
import math

def time_to_collision(x1, y1, d1, s1, x2, y2, d2, s2, r):
    dx = x2 - x1
    dy = y2 - y1
    dvx = s2 * math.sin(math.radians(d2)) - s1 * math.sin(math.radians(d1))
    dvy = s2 * math.cos(math.radians(d2)) - s1 * math.cos(math.radians(d1))
    a = dvx * dvx + dvy * dvy
    b = 2 * (dx * dvx + dy * dvy)
    c = dx * dx + dy * dy - r * r
    discriminant = b * b - 4 * a * c
    
    if a == 0:
        if b == 0:
            return float('inf')
        else:
            t = -c / b
            return t if t > 0 else float('inf')
    else:
        if discriminant < 0:
            return float('inf')
        t1 = (-b - math.sqrt(discriminant)) / (2 * a)
        t2 = (-b + math.sqrt(discriminant)) / (2 * a)
        
        if t1 > 0 and t2 > 0:
            return min(t1, t2)
        elif t1 > 0:
            return t1
        elif t2 > 0:
            return t2
        else:
            return float('inf')

def main():
    for line in sys.stdin:
        c = int(line)
        for _ in range(c):
            n, r = map(float, input().split())
            min_collision_time = float('inf')
            boats = []
            for _ in range(int(n)):
                x, y, d, s = map(float, input().split())
                boats.append((x, y, d, s))
            for i in range(len(boats)):
                x1, y1, d1, s1 = boats[i]
                for j in range(i + 1, len(boats)):
                    x2, y2, d2, s2 = boats[j]
                    time = time_to_collision(x1, y1, d1, s1, x2, y2, d2, s2, r)
                    min_collision_time = min(min_collision_time, time)
            if min_collision_time == float('inf'):
                print("No collision.")
            else:
                print(round(min_collision_time))

if __name__ == "__main__":
    main()
