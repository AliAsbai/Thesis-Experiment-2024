import sys

def winning_instances(n, board):
    dp = [0] * n

    # Initialize the dynamic programming array
    dp[0] = 1 if board[0] == 0 else 0

    # Update the dynamic programming array
    for i in range(1, n):
        for j in range(max(0, i - abs(board[i])), i):
            dp[i] += dp[j]
            if dp[i] >= 10**9 + 7:
                dp[i] -= 10**9 + 7

        if board[i] == 0:
            dp[i] += 1

    # Return the total count of winning instances
    return sum(dp) % (10**9 + 7)

def main():
    data = sys.stdin.read().strip().split('\n')
    n = int(data[0])
    board = list(map(int, data[1].split()))
    print(winning_instances(n, board))

if __name__ == "__main__":
    main()
