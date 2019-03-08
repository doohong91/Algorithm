T = int(input())
for tc in range(1,T+1):
    N = int(input())
    result = 0
    for _ in range(N):
        l,r = map(int, input().split())
        result += r-l+1
    print('#{} {}'.format(tc, result))