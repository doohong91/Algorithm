T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    area = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sums = 0
            for r in range(M):
                for c in range(M):
                    sums += area[i+r][j+c]
            if sums > result:
                result = sums
    print('#{} {}'.format(tc, result))