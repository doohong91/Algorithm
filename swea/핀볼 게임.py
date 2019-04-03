def play(y, x, a, b, p):
    global ans, N, row, col
    if 0 <= y < N and 0 <= x < N:
        loc = pan[y][x]
        if loc == -1 or (y == row and x == col):
            if ans < p:
                ans = p
            return
        elif loc == 0:
            if 0 <= y+a < N and 0 <= x+b < N:
                play(y + a, x + b, a, b, p)
            else:
                play(y - a, x - b, -a, -b, p + 1)
        elif loc == 1:
            if a == 1 and b == 0:
                play(y, x + 1, 0, 1, p+1)
            elif a == 0 and b == -1:
                play(y - 1, x, -1, 0, p + 1)
            else:
                play(y - a, x - b, -a, -b, p + 1)
        elif loc == 2:
            if a == -1 and b == 0:
                play(y, x + 1, 0, 1, p+1)
            elif a == 0 and b == -1:
                play(y + 1, x, 1, 0, p + 1)
            else:
                play(y - a, x - b, -a, -b, p + 1)
        elif loc == 3:
            if a == -1 and b == 0:
                play(y, x - 1, 0, -1, p+1)
            elif a == 0 and b == 1:
                play(y + 1, x, 1, 0, p + 1)
            else:
                play(y - a, x - b, -a, -b, p + 1)
        elif loc == 4:
            if a == 1 and b == 0:
                play(y, x - 1, 0, -1, p+1)
            elif a == 0 and b == 1:
                play(y - 1, x, -1, 0, p + 1)
            else:
                play(y - a, x - b, -a, -b, p + 1)
        elif loc == 5:
            play(y - a, x - b, -a, -b, p + 1)
        elif loc > 5:
            for w in wh[loc]:
                if w != [y, x]:
                    play(w[0]+a, w[1]+b, a, b, p)


path = [(-1, 0), (1, 0), (0, -1), (0, 1)]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pan = [0]*N
    wh = [[] for _ in range(11)]
    for i in range(N):
        pan[i] = list(map(int, input().split()))
        if 6 in pan[i]:
            wh[6].append([i, pan[i].index(6)])
        if 7 in pan[i]:
            wh[7].append([i, pan[i].index(7)])
        if 8 in pan[i]:
            wh[8].append([i, pan[i].index(8)])
        if 9 in pan[i]:
            wh[9].append([i, pan[i].index(9)])
        if 10 in pan[i]:
            wh[10].append([i, pan[i].index(10)])
    rows = [(N - 1, -1, -1), (N,), (N,), (N,)]
    cols = [(N,), (N,), (N - 1, -1, -1), (N,)]
    ans = 0
    for i in range(4):
        a, b = path[i]
        v = [[0]*N for _ in range(N)]
        for row in range(*rows[i]):
            for col in range(*cols[i]):
                if pan[row][col] == 0 and 0 <= row+a < N and 0 <= col+b < N and v[row+a][col+b] == 0:
                    v[row][col] = 1
                    play(row+a, col+b, a, b, 0)
    print(f'#{tc} {ans}')
