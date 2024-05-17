def calculate_fraction(t, a, b):
    numerator = t ** a - 1
    denominator = t ** b - 1
    return numerator, denominator

def is_integer_with_less_than_100_digits(t, a, b):
    numerator, denominator = calculate_fraction(t, a, b)
    result = numerator / denominator
    
    if len(str(int(result))) < 100:
        return f"({t}^{a}-1)/({t}^{b}-1) {int(result)}"
    else:
        return f"({t}^{a}-1)/({t}^{b}-1) is not an integer with less than 100 digits."

if __name__ == "__main__":
    while True:
        try:
            t, a, b = map(int, input().strip().split())
            if t == 0 and a == 0 and b == 0:
                break
            print(is_integer_with_less_than_100_digits(t, a, b))
        except EOFError:
            break
