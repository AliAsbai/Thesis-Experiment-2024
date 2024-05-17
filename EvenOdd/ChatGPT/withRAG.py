import sys

MOD = 10**9 + 7

def count_iterations(X):
    if X == 1:
        return 0
    if X % 2 == 0:
        return 1 + count_iterations(X // 2)
    else:
        return 1 + count_iterations(X + 1)

def main():
    for line in sys.stdin:
        L, R = map(int, line.split())
        
        # Calculate the sum of iterations
        result = 0
        for i in range(L, R + 1):
            result = (result + count_iterations(i)) % MOD
        
        print(result)

if __name__ == "__main__":
    main()
