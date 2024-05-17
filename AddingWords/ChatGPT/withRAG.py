import sys

def_val = {}  # Stores definitions of variables
val_def = {}  # Stores variables defined by those values

def evaluate_expression(expression):
    variables = expression.split()
    result = 0
    operator = '+'
    unknown_var = False
    for var in variables:
        if var == '+':
            operator = '+'
        elif var == '-':
            operator = '-'
        else:
            if var in val_def:
                if operator == '+':
                    result += val_def[var]
                elif operator == '-':
                    result -= val_def[var]
            else:
                unknown_var = True
                break
    if unknown_var:
        return 'unknown'
    return result

for line in sys.stdin:
    command = line.split()
    if command[0] == 'def':
        variable = command[1]
        value = int(command[2])
        def_val[variable] = value
        val_def[value] = variable
    elif command[0] == 'calc':
        expression = ' '.join(command[1:-1])
        result = evaluate_expression(expression)
        if result == 'unknown':
            print(expression + ' = ' + result)
        else:
            print(expression + ' = ' + val_def.get(result, 'unknown'))
    elif command[0] == 'clear':
        def_val.clear()
        val_def.clear()
