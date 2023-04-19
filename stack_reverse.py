def reverse_string(s):
    stack = []
    for c in s:
        stack.append(c)
    reversed_s = ""
    while len(stack) > 0:
        reversed_s += stack.pop()
    return reversed_s
s = "Hello, world!"
reversed_s = reverse_string(s)
print(reversed_s)
