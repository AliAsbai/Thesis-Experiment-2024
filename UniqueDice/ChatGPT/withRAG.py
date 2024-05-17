import sys

def canonical_representation(die):
    rotations = []
    for _ in range(4):
        rotations.append(die)
        die = (die[1], die[5], die[2], die[0], die[4], die[3])  # rotate top face clockwise
    die = (die[1], die[0], die[2], die[3], die[5], die[4])  # flip along top-bottom axis
    for _ in range(4):
        rotations.append(die)
        die = (die[1], die[5], die[2], die[0], die[4], die[3])  # rotate top face clockwise
    return min(rotations)

def main():
    dice_count = int(input())
    counts = {}
    
    for _ in range(dice_count):
        die = tuple(map(int, input().split()))
        canonical_die = canonical_representation(die)
        counts[canonical_die] = counts.get(canonical_die, 0) + 1
    
    max_count = max(counts.values())
    print(max_count)

if __name__ == "__main__":
    main()
