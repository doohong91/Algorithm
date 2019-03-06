M = int(input())
N = int(input())
v = []
for num in range(M,N+1):
    if num > 1:
        for a in range(2,num):
            if not num % a:
                num = 0
                break
        if num:
            v.append(num)
if v:
    print(f'{sum(v)}')
    print(f'{v[0]}')
else:
    print('-1')