#! /usr/bin/python3

def_val = {}  # Dictionary to store definitions (variable: value)
val_def = {}  # Dictionary to store defined values (value: variable)

for line in sys.stdin:
    # Split the line and remove leading/trailing whitespace
    command = line.strip().split()

    if command[0] == "def":
        # Definition command
        variable, value = command[1], int(command[2])
        def_val[variable] = value
        val_def[value] = variable  # Update value definition if it exists
    elif command[0] == "calc":
        # Calculation command
        expression = command[1:]
        result = calculate(expression)
        if result is not None:
            print(f"{'+'.join(expression)} = {result}")
        else:
            print(f"{'+'.join(expression)} = unknown")
    elif command[0] == "clear":
        # Clear command
        def_val.clear()
        val_def.clear()

def calculate(expression):
    # Function to evaluate the expression
    values = [def_val.get(word) for word in expression]  # Use get to avoid KeyError

    # Check if any word is not defined (None in values)
    if None in values:
        return None  # Word not defined

    # All words are defined, proceed with calculation
    result = values[0]
    for value in values[1:]:
        if "+" in expression:
            result += value
        elif "-" in expression:
            result -= value

    # Update val_def after calculation
    val_def[result] = expression[0]  # Use first word as the variable name

    return val_def.get(result)  # Use get to avoid KeyError if result not a defined word

