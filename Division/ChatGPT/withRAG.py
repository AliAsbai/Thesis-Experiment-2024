import sys

def calculate_formula(t, a, b):
    if b == 1:
        return t ** a - 1
    return (t ** a - 1) // (t ** b - 1)

def is_integer_less_than_100_digits(t, a, b):
    if (a - 1) % (t ** (b - 1)) == 0:
        return False
    numerator = t ** a - 1
    denominator = t ** b - 1
    if numerator % denominator == 0:
        result = numerator // denominator
        return len(str(result)) < 100
    return False

for line in sys.stdin:
    t, a, b = map(int, line.split())
    formula = f'({t}^{a}-1)/({t}^{b}-1)'
    if a % b == 0:
        print(f'{formula} {t ** (a // b) - 1}')
    elif is_integer_less_than_100_digits(t, a, b):
        print(f'{formula} {calculate_formula(t, a, b)}')
    else:
        print(f'{formula} is not an integer with less than 100 digits.')
