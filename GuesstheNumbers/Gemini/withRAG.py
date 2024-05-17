#! /usr/bin/python3

from collections import deque

def evaluate(expression, values, unknowns):
  """
  Evaluates the expression with assigned values to unknowns, considering operator precedence.

  Args:
    expression: The arithmetic expression string.
    values: A list of values to be assigned to unknowns.
    unknowns: A set of characters representing unknowns.

  Returns:
    The evaluated result of the expression, or None if invalid (including division by zero).
  """
  operators = "+-*/"
  stack = deque()
  for char in expression:
    if char in unknowns:
      index = unknowns.index(char)
      stack.append(values[index])
    elif char in operators:
      operand2 = stack.pop()
      operand1 = stack.pop()
      while len(stack) > 0 and stack[-1] not in "()" and \
          precedence(stack[-1], char) >= precedence(char, None):
        operator = stack.pop()
        operand2 = apply_operator(operator, stack.pop(), operand2)
      stack.append(operand2)
      stack.append(char)
    elif char == "(":
      stack.append(char)
    elif char == ")":
      while len(stack) > 0 and stack[-1] != "(":
        operator = stack.pop()
        operand2 = stack.pop()
        operand1 = stack.pop()
        stack.append(apply_operator(operator, operand1, operand2))
      stack.pop()  # Remove the "("
    else:
      return None
  while len(stack) > 1:
    operator = stack.pop()
    operand2 = stack.pop()
    operand1 = stack.pop()
    stack.append(apply_operator(operator, operand1, operand2))
  return stack.pop() if len(stack) == 1 else None

def apply_operator(operator, operand1, operand2):
  """
  Applies the operator to the operands.
  """
  if operator == "+":
    return operand1 + operand2
  elif operator == "-":
    return operand1 - operand2
  elif operator == "*":
    return operand1 * operand2
  elif operator == "/":
    if operand2 == 0:
      return None
    return operand1 / operand2
  else:
    return None  # Should not happen

def precedence(operator1, operator2):
  """
  Returns the precedence of an operator (higher is evaluated first).
  """
  precedence_map = {"*": 2, "/": 2, "+": 1, "-": 1, None: 0}
  return precedence_map[operator1] if operator1 else 0

def solve(test_case):
  """
  Solves a single test case for John's problem.

  Args:
    test_case: A tuple containing (num_unknowns, values, result, expression)

  Prints:
    "YES" if a solution exists, "NO" otherwise.
  """
  num_unknowns, values, result, expression = test_case
  unknowns = set(expression) - set("(+-*/().")
  for permutation in permutations(values, num_unknowns):
    evaluated
