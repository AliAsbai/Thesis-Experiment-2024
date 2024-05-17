import sys

def calculate_centroid(coordinates):
    n = len(coordinates)
    sum_x = sum(coord[0] for coord in coordinates)
    sum_y = sum(coord[1] for coord in coordinates)
    centroid_x = round(sum_x / n)
    centroid_y = round(sum_y / n)
    return centroid_x, centroid_y

def main():
    for line in sys.stdin:
        n = int(line.strip())
        if n == 0:
            break
        coordinates = []
        for _ in range(n):
            x, y = map(int, input().split())
            coordinates.append((x, y))
        centroid_x, centroid_y = calculate_centroid(coordinates)
        print(f"{centroid_x} {centroid_y}")

if __name__ == "__main__":
    main()
