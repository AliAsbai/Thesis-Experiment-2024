import sys

def min_moves_to_rearrange(n, s):
    # Count occurrences of each character
    A = s.count('A')
    B = s.count('B')
    C = s.count('C')

    # Calculate total number of characters
    total_chars = A + B + C

    # Function to calculate number of moves needed to fix a specific starting position
    def calc_moves(start_pos):
        moves = 0
        for i in range(3):
            # Calculate number of characters that need to be moved
            if i == 0:
                for j in range(A):
                    idx = (start_pos + j) % n
                    if s[idx] != 'A':
                        moves += 1
            elif i == 1:
                for j in range(B):
                    idx = (start_pos + A + j) % n
                    if s[idx] != 'B':
                        moves += 1
            else:
                for j in range(C):
                    idx = (start_pos + A + B + j) % n
                    if s[idx] != 'C':
                        moves += 1
        return moves

    # Iterate through possible starting positions for each character type
    min_moves = float('inf')
    for i in range(n):
        min_moves = min(min_moves, calc_moves(i))

    return min_moves

if __name__ == "__main__":
    for line in sys.stdin:
        n = int(line.strip())
        s = next(sys.stdin).strip()
        result = min_moves_to_rearrange(n, s)
        print(result)
