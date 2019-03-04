brac = [b for b in input()]
stack = []
result = 0
for b in brac:
    if b == '(':
        stack.append(')')
    elif b == '[':
        stack.append(']')
    elif stack:
        if stack[-1] == b:
            if b == ')':
                stack[-1] = 2
            else:
                stack[-1] = 3
        elif len(stack) > 1:
            if stack[-2] == b:
                if b == ')':
                    stack[-2] = stack[-1] * 2
                else:
                    stack[-2] = stack[-1] * 3
                stack.pop()
        if len(stack) > 1:
            if stack[-1] not in [']',')'] and stack[-2] not in [']',')']:
                stack[-2] += stack[-1]
                stack.pop()
    else:
        break
result = stack.pop()
if stack or result == '[' or result == ']':
    result = 0
print('{}'.format(result))