def evaluate(expression, values):
  """
  Evaluates the expression with a dictionary mapping unknowns to their values.

  Handles cases where:
    - Unknown has no assigned value.
    - Expression is invalid (e.g., division by zero).

  Returns:
      The evaluated result (float) or None if an error occurs.
  """
  operators = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "*": lambda a, b: a * b}
  stack = []
  for char in expression:
    if char.isalpha():
      # Unknown, replace with corresponding value from dictionary
      try:
        stack.append(values[char])
      except KeyError:
        # Unknown not assigned a value, return None to indicate error
        return None
    elif char in operators:
      # Pop operands and apply operator, handle division by zero
      operand2 = stack.pop()
      operand1 = stack.pop()
      if char == "/" and operand2 == 0:
        return None  # Division by zero error
      stack.append(operators[char](operand1, operand2))
    else:
      # Ignore parenthesis
      pass
  # Return the final result from the stack
  return stack[0]

def is_possible(unknowns, values, target, expression):
  """
  Checks if any assignment of values to unknowns makes expression evaluate to target.

  Handles cases where:
    - Number of values doesn't match unknowns.

  Returns:
      True if a valid assignment exists for the target value, False otherwise.
  """
  # Create a dictionary to map unknowns to their values
  assigned_values = dict(zip([chr(ord('a') + i) for i in range(unknowns)], values))
  # Evaluate the expression with assigned values
  result = evaluate(expression, assigned_values)
  # Check if evaluation returned an error or matches the target
  return result is not None and result == target

def main():
  while True:
    unknowns, *values_and_target = map(int, input().split())
    if unknowns == 0:
      break
    values, target = values_and_target[:unknowns], values_and_target[unknowns]
    expression = input()
    # Check if all unknowns have corresponding values
    if len(values) != unknowns:
      print("NO")
      continue
    print("YES" if is_possible(unknowns, values, target, expression) else "NO")

if __name__ == "__main__":
  main()
