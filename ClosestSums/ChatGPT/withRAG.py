import sys

def find_closest_sum(nums, query):
    nums.sort()
    closest_sum = float('inf')
    i, j = 0, len(nums) - 1
    
    while i < j:
        current_sum = nums[i] + nums[j]
        if abs(current_sum - query) < abs(closest_sum - query):
            closest_sum = current_sum
        
        if current_sum == query:
            return current_sum
        
        elif current_sum < query:
            i += 1
        else:
            j -= 1
    
    return closest_sum

case_number = 1
for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    
    nums = [int(sys.stdin.readline()) for _ in range(n)]
    m = int(sys.stdin.readline())
    
    print("Case {}:".format(case_number))
    for _ in range(m):
        query = int(sys.stdin.readline())
        closest_sum = find_closest_sum(nums, query)
        print("Closest sum to {} is {}.".format(query, closest_sum))
    
    case_number += 1
