def calculate_area(n, counts):
    size = 2 ** (-5/4)
    area = size ** 2
    for i in range(n-1):
        area *= 2 ** (-1/2)
    return area

def tape_length(n, counts):
    required_area = calculate_area(n, counts)
    available_area = 0
    for i in range(n-2, -1, -1):
        size = 2 ** (-5/4)
        for j in range(i, n-1):
            size *= 2 ** (-1/2)
        available_area += size ** 2 * counts[i]

    if available_area < required_area:
        return "impossible"
    
    length = 0
    for i in range(n-2, -1, -1):
        size = 2 ** (-5/4)
        for j in range(i, n-1):
            size *= 2 ** (-1/2)
        sheets_needed = math.ceil(required_area / (size ** 2))
        length += sheets_needed * size
        required_area /= 2
    
    return length

def main():
    n = int(input())
    counts = list(map(int, input().split()))

    result = tape_length(n, counts)
    print(result)

if __name__ == "__main__":
    import math
    main()
