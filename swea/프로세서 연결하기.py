def find_path(k, cal, point):
    global ans
    print(f'step {k}: {cal} {ans}')
    if k == len(P)-1 and ans > cal:
        ans = cal
        print('fin:', ans, cal)
        return
    elif k < len(P)-1 and ans > cal:
        x, y = point
        for a, b in path:
            cnt = found = 0
            while 0 <= x + a < N and 0 <= y + b < N and M[y + b][x + a] == 0:
                y += b
                x += a
                print(x, y, M[y][x])
                M[y][x] = -1
                cnt += 1
                if x in (0, N-1) or y in (0, N-1):
                    found = 1
            if found:
                print('next')
                find_path(k+1, cal + cnt, P[k+1])
            while cnt > 1:
                y -= b
                x -= a
                M[y][x] = 0
                cnt -= 1


path = [(0, -1), (0, 1), (-1, 0), (1, 0)]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [list(map(int, input().split())) for _ in range(N)]
    P = []
    for y in range(N):
        for x in range(N):
            if M[y][x] and x and y:
                P.append((x, y))
    P += [(0, 0)]
    ans = N * len(P)
    find_path(0, 0, P[0])
    print(f'#{tc} {ans}')

