import math

def will_collide(boat1, boat2, r):
    x1, y1, d1, s1 = boat1
    x2, y2, d2, s2 = boat2
    
    dx = x2 - x1
    dy = y2 - y1
    dist = math.sqrt(dx ** 2 + dy ** 2)
    if dist < r:
        return True
    return False

def seconds_to_collision(boats, r):
    min_time_to_collision = float('inf')
    for i in range(len(boats)):
        for j in range(i+1, len(boats)):
            if will_collide(boats[i], boats[j], r):
                dx = boats[j][0] - boats[i][0]
                dy = boats[j][1] - boats[i][1]
                dvx = boats[j][3] * math.sin(math.radians(boats[j][2])) - boats[i][3] * math.sin(math.radians(boats[i][2]))
                dvy = boats[j][3] * math.cos(math.radians(boats[j][2])) - boats[i][3] * math.cos(math.radians(boats[i][2]))
                dr = dx * dvx + dy * dvy
                dv = dvx * dvx + dvy * dvy
                if dv == 0:
                    continue
                t = -(dx * dvx + dy * dvy) / (dv)
                if t < 0:
                    continue
                min_time_to_collision = min(min_time_to_collision, t)
    
    if min_time_to_collision == float('inf'):
        print("No collision.")
    else:
        print(round(min_time_to_collision))

def main():
    c = int(input())
    for _ in range(c):
        n, r = map(float, input().split())
        boats = []
        for _ in range(int(n)):
            x, y, d, s = map(float, input().split())
            boats.append((x, y, d, s))
        seconds_to_collision(boats, r)

if __name__ == "__main__":
    main()
