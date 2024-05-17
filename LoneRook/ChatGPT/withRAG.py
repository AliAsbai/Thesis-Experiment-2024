import sys

def can_reach_target(board, rook_x, rook_y, target_x, target_y):
    r, c = len(board), len(board[0])
    # Check if the target square is attacked by any knight
    for dx, dy in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
        x, y = target_x + dx, target_y + dy
        if 0 <= x < r and 0 <= y < c and board[x][y] == 'K':
            return False

    # Check if there's a path from the rook to the target square
    visited = set()
    stack = [(rook_x, rook_y)]
    while stack:
        x, y = stack.pop()
        if (x, y) == (target_x, target_y):
            return True
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            while 0 <= new_x < r and 0 <= new_y < c and board[new_x][new_y] != 'K':
                stack.append((new_x, new_y))
                new_x, new_y = new_x + dx, new_y + dy
    return False

def main():
    for line in sys.stdin:
        r, c = map(int, line.split())
        board = [input() for _ in range(r)]
        rook_x, rook_y = None, None
        target_x, target_y = None, None

        for i in range(r):
            for j in range(c):
                if board[i][j] == 'R':
                    rook_x, rook_y = i, j
                elif board[i][j] == 'T':
                    target_x, target_y = i, j

        if can_reach_target(board, rook_x, rook_y, target_x, target_y):
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()
