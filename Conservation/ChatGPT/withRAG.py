import sys
from collections import defaultdict

def min_transport(t, test_cases):
    results = []
    
    for _ in range(t):
        n, m = test_cases[_][0]
        stages = test_cases[_][1]
        dependencies = test_cases[_][2]
        
        lab1, lab2 = [], []
        
        for i in range(n):
            if stages[i] == 1:
                lab1.append(i)
            else:
                lab2.append(i)
        
        dp = [[float('inf')] * (len(lab2) + 1) for _ in range(len(lab1) + 1)]
        dp[0][0] = 0
        
        for i in range(len(lab1) + 1):
            for j in range(len(lab2) + 1):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + (1 if (lab1[i - 1], lab1[i]) in dependencies else 0))
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + (1 if (lab2[j - 1], lab2[j]) in dependencies else 0))
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + (1 if (lab1[i - 1], lab2[j - 1]) in dependencies else 0))
        
        results.append(dp[len(lab1)][len(lab2)])
    
    return results

if __name__ == "__main__":
    test_cases = []
    t = int(input().strip())
    
    for _ in range(t):
        n, m = map(int, input().strip().split())
        stages = list(map(int, input().strip().split()))
        dependencies = [tuple(map(int, input().strip().split())) for _ in range(m)]
        test_cases.append(((n, m), stages, dependencies))
    
    results = min_transport(t, test_cases)
    
    for result in results:
        print(result)
