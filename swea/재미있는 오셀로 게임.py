def play(og,df,cnt1,cnt2):
    global N, x, y
    path = []
    for d in dirs:
        a,b = d
        if 0 <= x+a < N+1 and 0 <= y+b < N+1:
            if pan[y+b][x+a] == df:
                path.append((a,b))
    while path:
        a1,b1 = path.pop(0)
        a = a1
        b = b1
        stack = [(a,b)]
        while 1:
            a += a1
            b += b1
            if 0 <= x+a < N+1 and 0 <= y+b < N+1:
                if pan[y+b][x+a] == df:
                    stack.append((a,b))
                else:
                    stack.append((a,b))
                    break
            else: break
        a,b = stack.pop()
        if pan[y+b][x+a] == og:
            while stack:
                a,b = stack.pop()
                pan[y+b][x+a] = og
                cnt1 += 1
                cnt2 -= 1
    return cnt1, cnt2

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    pan = [[0]*(N+1) for _ in range(N+1)]
    pan[N//2][N//2] = 2
    pan[N//2+1][N//2+1] = 2
    pan[N//2][N//2+1] = 1
    pan[N//2+1][N//2] = 1
    cnt1 = cnt2 = 2
    dirs = [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(1,-1),(-1,1),(1,1)]
    for _ in range(M):
        x,y,c = map(int,input().split())
        pan[y][x] = c
        if c == 1:
            cnt1 += 1
            cnt1,cnt2 = play(c,2,cnt1,cnt2)
        else:
            cnt2 += 1
            cnt2,cnt1 = play(c,1,cnt2,cnt1)
    print('#{} {} {}'.format(tc, cnt1, cnt2))        