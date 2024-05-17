def count_guests(R, C, layout):
    def is_valid(x, y):
        return 0 <= x < R and 0 <= y < C

    guests = 0

    for i in range(R):
        for j in range(C):
            if layout[i][j] == '.':
                perimeter = 0
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = i + dx, j + dy
                    if is_valid(nx, ny) and layout[nx][ny] == '.':
                        perimeter += 1
                guests = max(guests, perimeter)

    return guests

# Sample Input 1
R1, C1 = 2, 2
layout1 = ["..", ".."]
print(count_guests(R1, C1, layout1))  # Output: 7

# Sample Input 2
R2, C2 = 4, 4
layout2 = ["X.XX", "X..X", "..X.", "..XX"]
print(count_guests(R2, C2, layout2))  # Output: 9

# Sample Input 3
R3, C3 = 3, 3
layout3 = ["X.X", ".X.", "X.X"]
print(count_guests(R3, C3, layout3))  # Output: 3
