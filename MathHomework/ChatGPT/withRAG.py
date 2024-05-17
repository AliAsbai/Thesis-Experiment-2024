import sys

def count_seat_adjustments(sequence, policy):
    adjustments = 0
    current_seat_position = sequence[0]
    
    for preference in sequence[1:]:
        if current_seat_position != preference:
            adjustments += 1
            if policy == 3:  # For policy 3, adjust the seat as you leave
                current_seat_position = preference
        elif policy == 3:  # For policy 3, adjust the seat as you leave
            current_seat_position = preference
    
    if policy == 1 or policy == 2:
        adjustments += 1  # Adjust the seat as you leave to match the policy
    
    return adjustments

if __name__ == "__main__":
    sequence = input().strip().split()
    for i in range(len(sequence) - 1):
        initial_position = sequence[i]
        preferences = sequence[i + 1]
        
        policy_1_adjustments = count_seat_adjustments(preferences, 1)
        policy_2_adjustments = count_seat_adjustments(preferences, 2)
        policy_3_adjustments = count_seat_adjustments(preferences, 3)
        
        print(policy_1_adjustments, end=" ")
        print(policy_2_adjustments, end=" ")
        print(policy_3_adjustments)
