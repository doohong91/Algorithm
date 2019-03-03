brac = [b for b in input()]
stack = []
result = score = 0
for b in brac:
    print(score,result)
    if b == '(':
        if not stack:
            result += score
            score = 1
        stack.append(')')
    elif b == '[':
        if not stack:
            result += score
            score = 1
        stack.append(']')
    elif stack:
        if stack[-1] == b:
            if b == ')':
                score *= 2
                stack.pop()
            else: 
                score *= 3
                stack.pop()
        else:
            result = 0
            break
    else:
        result = 0
        break
if stack:
    result = 0
print(f'{result}')