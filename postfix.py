def evaluate_postfix(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if char == '+':
                stack.append(op1 + op2)
            elif char == '-':
                stack.append(op1 - op2)
            elif char == '*':
                stack.append(op1 * op2)
            elif char == '/':
                stack.append(op1 / op2)
    return stack.pop()
expression = "34+2*"
result = evaluate_postfix(expression)
print(result)
