from sympy import symbols, Eq, solve, simplify

def solve_linear_equations(test_cases):
    for equations in test_cases:
        eq1, eq2 = equations.strip().split('\n')
        
        # Parse equations into SymPy format
        x, y = symbols('x y')
        eq1_parts = eq1.split('=')
        eq2_parts = eq2.split('=')
        eq1_sympy = Eq(eval(eq1_parts[0]), eval(eq1_parts[1]))
        eq2_sympy = Eq(eval(eq2_parts[0]), eval(eq2_parts[1]))

        # Solve the equations
        solution = solve((eq1_sympy, eq2_sympy), (x, y))
        
        # Check if solution exists and print accordingly
        if solution:
            x_val = simplify(solution[x]).as_numer_denom()
            y_val = simplify(solution[y]).as_numer_denom()
            if x_val[1] == 1 and y_val[1] == 1:
                print(x_val[0])
                print(y_val[0])
            else:
                print(f"{x_val[0]}/{x_val[1]}")
                print(f"{y_val[0]}/{y_val[1]}")
        else:
            print("don't know")
        print()

# Example usage
test_cases = [
    "2*x + 3*y = x\n5 = x + y + 3\n",
    "2*x + 3*y = 0\n10*x = -15*y\n",
    "2*x + 3*y = 0\n10*x = -15*y + 1\n",
    "x = 1\n3*x = 6*y\n",
    "2*x = 3*x + -x + y\nx + y = x + y\n",
    "2*x = -3\n-2*y = 3\n",
    "1 = 2\nx = 3\n"
]

solve_linear_equations(test_cases)
