def count_seat_adjustments(prefs):
    total_adjust_up = 0
    total_adjust_down = 0
    total_adjust_own = 0

    current_state = prefs[0]

    for preference in prefs[1:]:
        if preference != current_state:
            if preference == 'U':
                total_adjust_down += 1
            else:
                total_adjust_up += 1
            total_adjust_own += 1

        current_state = preference

    # Adjustments needed for the last person's preference
    if prefs[-1] == 'U':
        total_adjust_up += 1
    else:
        total_adjust_down += 1

    # Adjustments needed for the policy "leave the seat as you would like to find it"
    total_adjust_own += min(total_adjust_up, total_adjust_down)

    return total_adjust_up, total_adjust_down, total_adjust_own

# Reading input
sequence = input().strip()

# Calculating adjustments
up_adjustments, down_adjustments, own_adjustments = count_seat_adjustments(sequence)

# Outputting results
print(up_adjustments)
print(down_adjustments)
print(own_adjustments)
