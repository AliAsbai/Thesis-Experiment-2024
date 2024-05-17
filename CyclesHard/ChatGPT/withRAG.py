import sys

def count_hamiltonian_cycles(n, forbidden_edges):
    # Create a table to store the counts of Hamiltonian cycles
    # dp[i][mask] represents the number of Hamiltonian cycles ending at node i
    # with visited nodes represented by the binary mask
    dp = [[0] * (1 << n) for _ in range(n)]
    
    # Initialize the table for the base case (starting from node 0)
    dp[0][1] = 1
    
    # Iterate over all possible subsets of visited nodes
    for mask in range(1, 1 << n):
        for i in range(n):
            # Check if node i is in the current subset
            if mask & (1 << i):
                for j in range(n):
                    # Check if there is an edge from j to i and j is in the subset
                    if i != j and mask & (1 << j) and (j + 1, i + 1) not in forbidden_edges:
                        dp[i][mask] += dp[j][mask ^ (1 << i)]
    
    # The result is the sum of counts of Hamiltonian cycles ending at each node n-1
    total_cycles = sum(dp[i][(1 << n) - 1] for i in range(n) if (i + 1, 1) not in forbidden_edges)
    return total_cycles % 9901

def main():
    case_number = 1
    for line in sys.stdin:
        t = int(line.strip())
        for _ in range(t):
            n, k = map(int, sys.stdin.readline().split())
            forbidden_edges = set()
            for _ in range(k):
                u, v = map(int, sys.stdin.readline().split())
                forbidden_edges.add((u, v))
                forbidden_edges.add((v, u))  # Adding the reverse edge as well
            total_cycles = count_hamiltonian_cycles(n, forbidden_edges)
            print("Case #{}: {}".format(case_number, total_cycles))
            case_number += 1

if __name__ == "__main__":
    main()
