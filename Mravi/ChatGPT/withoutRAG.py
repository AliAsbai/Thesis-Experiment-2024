class Node:
    def __init__(self, ki):
        self.children = []
        self.flow = []
        self.superpower = []
        self.ki = ki
        self.total_ki = 0

def dfs(node, l):
    if not node.children:
        node.total_ki = node.ki
        return node.ki

    total_ki = 0
    for child, flow, superpower in zip(node.children, node.flow, node.superpower):
        child_ki = dfs(child, l)
        if superpower == 1:
            child_ki = child_ki ** 2
        total_ki += child_ki * flow / 100

    node.total_ki = min(node.ki, total_ki)
    return node.total_ki

def main():
    n = int(input().strip())
    nodes = [Node(-1) for _ in range(n+1)]

    for _ in range(n-1):
        a, b, flow, superpower = map(int, input().split())
        nodes[a].children.append(nodes[b])
        nodes[a].flow.append(flow)
        nodes[a].superpower.append(superpower)

    ki_values = list(map(float, input().split()))

    for i, ki in enumerate(ki_values, 1):
        nodes[i].ki = ki

    l = float(input().strip())
    dfs(nodes[1], l)

    print("{:.4f}".format(max(0, nodes[1].total_ki - l)))

if __name__ == "__main__":
    main()
