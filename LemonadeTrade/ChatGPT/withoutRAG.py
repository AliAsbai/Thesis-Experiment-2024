from collections import defaultdict


def max_blue_lemonade(N, trades):
    graph = defaultdict(list)

    # Build the graph
    for trade in trades:
        offered, wanted, rate = trade
        if wanted == 'pink':
            graph[offered].append((wanted, rate))

    # DFS to find the maximum blue lemonade
    def dfs(lemonade, amount):
        nonlocal max_blue
        if lemonade == 'blue':
            max_blue = min(max_blue, amount)
            return
        for next_lemonade, rate in graph[lemonade]:
            dfs(next_lemonade, amount * rate)

    max_blue = float('inf')
    dfs('blue', 10)

    return 10 - max_blue if max_blue != float('inf') else 0


# Input parsing
N = int(input())
trades = []
for _ in range(N):
    O, W, R = input().split()
    R = float(R)
    trades.append((O, W, R))

# Output result
result = max_blue_lemonade(N, trades)
print("{:.15f}".format(result))
