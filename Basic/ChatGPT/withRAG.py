import sys

def is_valid_integer_constant(s):
    if s.isdigit():  # Check if it's a decimal integer
        return True
    if '#' not in s:  # If '#' is not present, it's not a valid format
        return False
    
    base, digits = s.split('#')[0], s.split('#')[1]
    
    # Check if base is a valid integer between 2 and 16
    try:
        base_val = int(base)
        if base_val < 2 or base_val > 16:
            return False
    except ValueError:
        return False
    
    # Check if digits are valid for the specified base
    if base_val <= 10:
        valid_digits = set(str(i) for i in range(base_val))
    else:
        valid_digits = set(str(i) for i in range(10)) | set(chr(i) for i in range(ord('a'), ord('a') + base_val - 10))
    
    # Check if all characters in digits are valid
    for d in digits.lower():
        if d not in valid_digits:
            return False
    
    # Check if there are additional characters after the digits and the '#'
    if len(s.split('#')) > 2:
        return False
    
    return True

# Read input
lines = sys.stdin.readlines()
n = int(lines[0].strip())
for line in lines[1:]:
    data = line.strip()
    if is_valid_integer_constant(data):
        print("yes")
    else:
        print("no")
