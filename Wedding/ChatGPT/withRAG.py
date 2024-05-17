import sys

def solve_seating(n, m, adulterous_pairs):
    bride_side = set(range(1, n))  # Initialize bride's side with all guests except groom

    # Initialize a dictionary to store spouses
    spouses = {}
    for pair in adulterous_pairs:
        spouse1, spouse2 = pair.split()
        spouse1_id, spouse1_gender = int(spouse1[:-1]), spouse1[-1]
        spouse2_id, spouse2_gender = int(spouse2[:-1]), spouse2[-1]

        # Check if spouses are from the same side
        if (spouse1_gender == 'h' and spouse2_gender == 'w') or (spouse1_gender == 'w' and spouse2_gender == 'h'):
            if spouse1_id in bride_side and spouse2_id in bride_side:
                return "bad luck"

        spouses[spouse1_id] = spouse2_id
        spouses[spouse2_id] = spouse1_id

    # Check if any spouses are on bride's side
    for guest in bride_side.copy():
        if guest in spouses:
            bride_side.discard(spouses[guest])

    return ' '.join(str(guest) + 'h' for guest in sorted(bride_side))

def main():
    for line in sys.stdin:
        n, m = map(int, line.split())
        adulterous_pairs = [input().strip() for _ in range(m)]
        result = solve_seating(n, m, adulterous_pairs)
        print(result)

if __name__ == "__main__":
    main()
