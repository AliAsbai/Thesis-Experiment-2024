import sys

def smallest_toolbar_area(N, sizes):
    sizes.sort()  # Sort the sizes in ascending order
    row1 = sizes[:N]  # Sizes for the first row
    row2 = sizes[N:]  # Sizes for the second row

    max_height = max(sum(row1), sum(row2))  # Max height of the toolbar
    max_width = max(max(row1), max(row2))  # Max width of the toolbar

    return max_height * max_width

def main():
    N = int(sys.stdin.readline().strip())
    sizes = [int(sys.stdin.readline().strip()) for _ in range(2 * N)]
    print(smallest_toolbar_area(N, sizes))

if __name__ == "__main__":
    main()
