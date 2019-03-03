T = int(input())
for tc in range(T):
    brac = [b for b in input()]
    stack = []
    ans = 'YES'
    for b in brac:
        if b == '(':
            stack.append(')')
        elif stack:
            if stack[-1] == b:
                stack.pop()
            else:
                ans = 'NO'
                break
        else:
            ans = 'NO'
            break
    if stack:
        ans = 'NO'
    print(ans)