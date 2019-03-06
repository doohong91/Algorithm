T = int(input())
for tc in range(1,T+1):
    N = int(input())
    m = N // 2
    result = 0
    for i in range(N):
        if i > m:
            k = N-i-1
        else:
            k = i
        farm = [int(num) for num in input()]
        for j in range(m-k,m+k+1):
            result += farm[j]
    print('#{} {}'.format(tc, result))