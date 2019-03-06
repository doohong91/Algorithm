testcase = int(input())
for t in range(testcase):
    a,b = map(int,input().split())
    dist = b-a
    n = 1
    cnt = 0
    while 1:
        pow_n = n**2
        min_n = pow_n - n + 1
        max_n = pow_n + n
        if dist in range(min_n,max_n+1):
            if dist in range(min_n,pow_n+1):
                cnt = 2*n - 1
            else:
                cnt = 2*n
            break
        n += 1
    print(cnt)