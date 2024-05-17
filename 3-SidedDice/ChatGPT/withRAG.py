import sys
import numpy as np

def is_feasible(dice_probabilities, desired_probabilities):
    A = np.array(dice_probabilities)
    b = np.array(desired_probabilities)
    x = np.linalg.lstsq(A, b, rcond=None)[0]
    return all(x >= 0) and np.isclose(sum(x), 1)

def main():
    for line in sys.stdin:
        dice1 = list(map(int, line.split()))
        dice2 = list(map(int, sys.stdin.readline().split()))
        dice3 = list(map(int, sys.stdin.readline().split()))
        desired = list(map(int, sys.stdin.readline().split()))

        if sum(dice1) == 0 and sum(dice2) == 0 and sum(dice3) == 0:
            break

        dice_probabilities = [dice1, dice2, dice3]

        if is_feasible(dice_probabilities, desired):
            print("YES")
        else:
            print("NO")
        sys.stdin.readline()  # Read the blank line separating test cases

if __name__ == "__main__":
    main()
