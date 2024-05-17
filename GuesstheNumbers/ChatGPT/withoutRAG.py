def evaluate(expression, values):
    stack = []
    for char in expression:
        if char.islower():
            stack.append(values[char])
        elif char in {'+', '-', '*'}:
            stack.append(char)
        elif char == '(':
            stack.append('(')
        elif char == ')':
            sub_exp = []
            while stack[-1] != '(':
                sub_exp.append(stack.pop())
            stack.pop()  # Remove '('
            stack.append(str(eval(''.join(sub_exp[::-1]))))
    return int(stack[0])


def assign_values(expression, unknowns, values, result):
    if not unknowns:
        return evaluate(expression, values) == result
    unknown = unknowns.pop()
    for value in values:
        values[unknown] = value
        if assign_values(expression, unknowns, values, result):
            return True
    unknowns.add(unknown)
    return False


def main():
    while True:
        n, *values, result = map(int, input().split())
        if n == 0 and result == 0:
            break
        values_dict = {chr(ord('a') + i): values[i] for i in range(n)}
        expression = input().strip()
        unknowns = set(char for char in expression if char.islower())
        if assign_values(expression, unknowns, values_dict, result):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
