def find_cooking_time(N, M, entry_times, exit_times):
    max_correspondences = 0
    best_cooking_time = 0

    for entry_time in entry_times:
        correspondences = 0
        for exit_time in exit_times:
            time_diff = exit_time - entry_time
            count = sum(1 for e_time in entry_times if e_time + time_diff in exit_times)
            correspondences = max(correspondences, count)
        
        if correspondences > max_correspondences:
            max_correspondences = correspondences
            best_cooking_time = entry_time

    return best_cooking_time


# Read input
N = int(input())
M = int(input())
entry_times = list(map(int, input().split()))
exit_times = list(map(int, input().split()))

# Call the function and print the result
result = find_cooking_time(N, M, entry_times, exit_times)
print(result)
