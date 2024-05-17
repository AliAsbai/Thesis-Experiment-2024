def closest_sum(nums, query):
    nums.sort()  # Sort the numbers for efficient two-pointer approach
    left, right = 0, len(nums) - 1
    closest_diff = float('inf')
    closest_sum = None

    # Check if any single number is the closest sum
    if query in nums:
        return query

    while left < right:
        current_sum = nums[left] + nums[right]
        current_diff = abs(current_sum - query)

        if current_diff < closest_diff:
            closest_diff = current_diff
            closest_sum = current_sum

        if current_sum < query:
            left += 1  # Need a larger sum, move left pointer
        else:
            right -= 1  # Need a smaller sum, move right pointer

    # Handle cases where no closest sum exists (pointers never meet)
    if closest_sum is None:
        closest_sum = query

    return closest_sum

# Process input cases
while True:
    n = int(input())
    if n == 0:  # End of input
        break

    nums = [int(input()) for _ in range(n)]
    m = int(input())
    queries = [int(input()) for _ in range(m)]

    case_num = 1
    print("Case", case_num, ":")
    for query in queries:
        closest = closest_sum(nums, query)
        print("Closest sum to", query, "is", closest)

    case_num += 1
