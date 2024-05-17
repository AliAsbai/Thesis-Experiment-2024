MOD = 1000000007

def count_inversions(s):
    n = len(s)
    total_inversions = 0
    question_marks_to_left = 0
    ones_to_right = 0
    
    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            ones_to_right += 1
            total_inversions = (total_inversions + question_marks_to_left) % MOD
        elif s[i] == '0':
            total_inversions = (total_inversions + ones_to_right) % MOD
        else:  # s[i] == '?'
            total_inversions = (total_inversions * 2 + ones_to_right) % MOD
            question_marks_to_left = (question_marks_to_left * 2 + 1) % MOD
    
    return total_inversions

# Input
s = input().strip()

# Output
print(count_inversions(s))
