import sys

def calculate_candles_needed(N):
    return (N * (N + 1) // 2) + N

def main():
    for line in sys.stdin:
        P = int(line)
        for _ in range(P):
            data_set, N = map(int, input().split())
            candles_needed = calculate_candles_needed(N)
            print(data_set, candles_needed)

if __name__ == "__main__":
    main()
