def parse_equation(equation):
    terms = equation.split()
    x_coefficient = 0
    y_coefficient = 0
    constant = 0

    for term in terms:
        if 'x' in term:
            if term == 'x':
                x_coefficient += 1
            elif term == '-x':
                x_coefficient -= 1
            else:
                x_coefficient += int(term[:-1])
        elif 'y' in term:
            if term == 'y':
                y_coefficient += 1
            elif term == '-y':
                y_coefficient -= 1
            else:
                y_coefficient += int(term[:-1])
        else:
            constant += int(term)

    return x_coefficient, y_coefficient, -constant

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    gcd_value = gcd(numerator, denominator)
    return numerator // gcd_value, denominator // gcd_value

def solve_equations(eq1, eq2):
    x1, y1, c1 = parse_equation(eq1)
    x2, y2, c2 = parse_equation(eq2)

    determinant = x1 * y2 - x2 * y1

    if determinant == 0:  # If determinant is zero, equations are parallel or coincident
        if c1 == 0 and c2 == 0:  # If both constants are zero, equations are coincident
            print("don't know\ndon't know\n")
        else:
            print("don't know\ndon't know\n")
    else:
        x = (c1 * y2 - c2 * y1) / determinant
        y = (x1 * c2 - x2 * c1) / determinant
        x, y = simplify_fraction(x, y)
        print(f"{x}\n{y}\n")

# Read input until EOF
try:
    while True:
        num_test_cases = int(input())
        for _ in range(num_test_cases):
            eq1 = input().strip()
            eq2 = input().strip()
            solve_equations(eq1, eq2)
except EOFError:
    pass  # End of input
