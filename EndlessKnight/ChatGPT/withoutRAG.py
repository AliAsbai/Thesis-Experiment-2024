def knight_moves(h, w, rocks):
    MOD = 10007
    directions = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]
    dp = [[0] * (w+1) for _ in range(h+1)]
    dp[1][1] = 1
    for i in range(1, h+1):
        for j in range(1, w+1):
            if (i, j) in rocks:
                continue
            for dr, dc in directions:
                ni, nj = i + dr, j + dc
                if 1 <= ni <= h and 1 <= nj <= w and (ni, nj) not in rocks and ni > i and nj > j:
                    dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % MOD
    return dp[h][w]

def main():
    N = int(input().strip())
    for case in range(1, N+1):
        h, w, r = map(int, input().strip().split())
        rocks = set()
        for _ in range(r):
            ri, ci = map(int, input().strip().split())
            rocks.add((ri, ci))
        result = knight_moves(h, w, rocks)
        print(f"Case #{case}: {result}")

if __name__ == "__main__":
    main()
