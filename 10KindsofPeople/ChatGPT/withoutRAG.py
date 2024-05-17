def dfs(grid, visited, r, c, target_zone):
    rows = len(grid)
    cols = len(grid[0])
    
    if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or grid[r][c] != target_zone:
        return False
    
    visited[r][c] = True
    
    if r == rows - 1 or c == cols - 1 or r == 0 or c == 0:
        return True
    
    return any(dfs(grid, visited, r + dr, c + dc, target_zone) for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)])


def main():
    r, c = map(int, input().split())
    grid = [input() for _ in range(r)]

    n = int(input())
    for _ in range(n):
        r1, c1, r2, c2 = map(int, input().split())
        r1 -= 1
        c1 -= 1
        r2 -= 1
        c2 -= 1
        visited = [[False] * c for _ in range(r)]
        if grid[r1][c1] == grid[r2][c2]:
            print("binary" if grid[r1][c1] == '0' else "decimal")
        elif dfs(grid, visited, r1, c1, grid[r1][c1]):
            print("neither")
        else:
            print("binary" if grid[r1][c1] == '1' else "decimal")

if __name__ == "__main__":
    main()
