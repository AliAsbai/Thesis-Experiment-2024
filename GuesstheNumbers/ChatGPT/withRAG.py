import sys
from itertools import permutations

def evaluate_expression(expression, values):
    stack = []
    for char in expression:
        if char.islower():
            stack.append(values[char])
        elif char == '(':
            stack.append('(')
        elif char == ')':
            sub_expression = []
            while stack[-1] != '(':
                sub_expression.append(stack.pop())
            stack.pop()  # Pop '('
            sub_expression = sub_expression[::-1]  # Reverse to get correct order
            stack.append(evaluate_expression(sub_expression, values))
        else:  # Operator
            op2 = stack.pop()
            op1 = stack.pop()
            if char == '+':
                stack.append(op1 + op2)
            elif char == '-':
                stack.append(op1 - op2)
            elif char == '*':
                stack.append(op1 * op2)
    return stack[0]

def is_possible(expression, values, result):
    for perm in permutations(values):
        if evaluate_expression(expression, dict(zip(expression, perm))) == result:
            return "YES"
    return "NO"

for line in sys.stdin:
    n_values, *values, result = map(int, line.split())
    if n_values == 0:
        break
    expression = input().strip()
    print(is_possible(expression, values, result))
