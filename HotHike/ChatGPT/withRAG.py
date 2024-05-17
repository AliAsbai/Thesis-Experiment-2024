import sys

def find_best_hiking_days(n, temperatures):
    min_max_temp = float('inf')
    best_start_day = 1
    
    for i in range(2, n):
        max_temp = max(temperatures[i], temperatures[i-1])
        max_temp = max(max_temp, temperatures[i-2])
        
        if max_temp < min_max_temp:
            min_max_temp = max_temp
            best_start_day = i - 1
    
    return best_start_day, min_max_temp

if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    temperatures = list(map(int, data[1].split()))
    best_day, min_max_temp = find_best_hiking_days(n, temperatures)
    print(best_day, min_max_temp)
