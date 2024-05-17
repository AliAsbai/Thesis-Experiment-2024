def is_valid_integer_constant(s):
    if s.isdigit():
        return True
    if '#' in s:
        parts = s.split('#')
        if len(parts) == 3 and parts[0].isdigit() and parts[2].isdigit():
            base = int(parts[0])
            digits = parts[1]
            if 2 <= base <= 16:
                for digit in digits:
                    if digit.isdigit():
                        if int(digit) >= base:
                            return False
                    elif not ('a' <= digit.lower() <= 'f'):
                        return False
                return True
    return False

# Sample Input Processing
n = int(input())
for _ in range(n):
    line = input()
    if is_valid_integer_constant(line):
        print("yes")
    else:
        print("no")
