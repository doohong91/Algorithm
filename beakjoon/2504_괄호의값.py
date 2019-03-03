brac = [b for b in input()]
stack = []
result = score = 0
for b in brac:
    print(score,result)
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
        else:
            result = 0
            break
    else:
        result = 0
        break
if stack:
    result = 0
print(f'{result}')