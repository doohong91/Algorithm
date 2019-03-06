n = int(input())
nums = list(range(1,n+1))
stack = []
result = []
inputs = [int(input()) for _ in range(n)]
for num in inputs:
    if num not in stack:
        while num in nums:
            stack.append(nums.pop(0))
            result.append('+')
    try:
        if num in stack:
            for i in range(len(stack)):
                if stack[i] == num:
                    stack.pop(i)
                    result.append('-')
    except :
        result = ['NO']
        break
for r in result:
    print(r)           