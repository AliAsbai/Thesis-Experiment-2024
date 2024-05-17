def evaluate_calculation(calculation, variables):
    terms = calculation.split()
    result = 0
    operator = '+'
    unknown_terms = set()

    for term in terms:
        if term in ['+', '-']:
            operator = term
        else:
            if term not in variables:
                unknown_terms.add(term)
            else:
                if operator == '+':
                    result += variables[term]
                elif operator == '-':
                    result -= variables[term]

    if unknown_terms:
        return 'unknown'
    else:
        return result

def main():
    variables = {}

    while True:
        try:
            command = input().strip()
        except EOFError:
            break

        if command.startswith('def'):
            _, var, val = command.split()
            variables[var] = int(val)
        elif command.startswith('calc'):
            calculation = command.split('=')[0][5:].strip()
            result = evaluate_calculation(calculation, variables)
            print(f'{calculation} = {result}')
        elif command == 'clear':
            variables.clear()

if __name__ == "__main__":
    main()
