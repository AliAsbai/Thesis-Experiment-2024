import sys

def is_within_bounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def dfs(grid, r, c, visited, target):
    if not is_within_bounds(grid, r, c) or grid[r][c] != target or visited[r][c]:
        return 0

    visited[r][c] = True
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    area = 1
    for dr, dc in directions:
        area += dfs(grid, r + dr, c + dc, visited, target)
    return area

def normalize(grid):
    groups = {}
    group_num = 0
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j]:
                area = dfs(grid, i, j, visited, grid[i][j])
                groups[(i, j)] = (grid[i][j], area)

    return groups

def main():
    rows, cols = map(int, input().split())
    grid = [input() for _ in range(rows)]
    queries = int(input())

    groups = normalize(grid)

    for _ in range(queries):
        r1, c1, r2, c2 = map(int, input().split())
        if not is_within_bounds(grid, r1 - 1, c1 - 1) or not is_within_bounds(grid, r2 - 1, c2 - 1):
            print("neither")
            continue

        group_num_1 = (r1 - 1, c1 - 1)
        group_num_2 = (r2 - 1, c2 - 1)

        if group_num_1 in groups and group_num_2 in groups:
            if groups[group_num_1][0] == groups[group_num_2][0]:
                print("binary" if groups[group_num_1][0] == '0' else "decimal")
            else:
                print("neither")
        else:
            print("neither")

if __name__ == "__main__":
    main()
