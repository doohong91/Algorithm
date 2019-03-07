for _ in range(10):
    tc = int(input())
    lad = [list(map(int,input().split())) for _ in range(100)]
    X = []
    for i in range(100):
        if lad[0][i]:
            X.append(i)
    path = [(0,-1),(0,1),(1,0)]
    min_c = 10000
    ans = 0
    for sx in X:
        x = sx
        y = cnt = 0
        vis = [[0]*100 for _ in range(100)]
        while y < 99:
            vis[y][x] = 1
            for p in path:
                a,b = p
                if 0 <= y+a < 100 and 0 <= x+b < 100:
                    if lad[y+a][x+b] and not vis[y+a][x+b]:
                        x += b
                        y += a
                        cnt += 1
        if min_c >= cnt:
            min_c = cnt
            ans = sx
    print('#{} {}'.format(tc, ans))