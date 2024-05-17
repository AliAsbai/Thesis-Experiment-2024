import sys

def main():
    # Read input
    n = int(input().strip())
    m = int(input().strip())
    entry_times = list(map(int, input().strip().split()))
    exit_times = list(map(int, input().strip().split()))

    # Compute time differences
    diffs = {}
    for entry_time in entry_times:
        for exit_time in exit_times:
            diff = exit_time - entry_time
            if diff >= 0:
                diffs[diff] = diffs.get(diff, 0) + 1

    # Find the most frequent positive difference
    max_freq = 0
    best_guess = 0
    for diff, freq in diffs.items():
        if freq > max_freq:
            max_freq = freq
            best_guess = diff
        elif freq == max_freq and diff < best_guess:
            best_guess = diff

    # Output the best guess
    print(best_guess)

if __name__ == "__main__":
    main()
