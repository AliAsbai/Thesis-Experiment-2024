#! /usr/bin/python3

def parse_expression(expression_str):
  """
  Parses a tower of powers expression into a list of (base, exponent) tuples.
  """
  expression = []
  for token in expression_str.split('^'):
    expression.append((int(token[0]), int(token[1:])))
  return expression

def evaluate_expression(expression):
  """
  Evaluates a tower of powers expression using a loop.
  """
  value = 1
  for base, exponent in expression:
    value *= base**exponent
  return value

def sort_by_value(data):
  """
  Sorts expressions based on their evaluated value.
  """
  return sorted(data, key=evaluate_expression)

def main():
  """
  Reads input, sorts numbers, and prints the sorted list.
  """
  case_number = 1
  for line in sys.stdin:
    num_elements = int(line)
    expressions = []
    for _ in range(num_elements):
      expression_str = sys.stdin.readline().strip()
      expression = parse_expression(expression_str)
      expressions.append(expression)
    sorted_expressions = sort_by_value(expressions)
    
    print(f"Case {case_number}:")
    for expression in sorted_expressions:
      expression_str = "^".join([f"{base}^{exponent}" for base, exponent in expression])
      print(expression_str)
    case_number += 1

if __name__ == "__main__":
  main()
