def play(y, x, a, b, p):
    global ans, N, row, col
    while 0 <= y < N and 0 <= x < N:
        loc = pan[y][x]
        a1 = a
        b1 = b
        # print('({},{}) {} [{},{}] {}'.format(y, x, loc, a, b, p), row, col)
        if loc == -1 or (y == row and x == col):
            if ans < p:
                ans = p
            return
        elif loc == 1:
            if a == 1 and b == 0:
                a, b = path[3]
            elif a == 0 and b == -1:
                a, b = path[0]
            else:
                a *= -1
                b *= -1
            p += 1
        elif loc == 2:
            if a == -1 and b == 0:
                a, b = path[3]
            elif a == 0 and b == -1:
                a, b = path[1]
            else:
                a *= -1
                b *= -1
            p += 1
        elif loc == 3:
            if a == -1 and b == 0:
                a, b = path[2]
            elif a == 0 and b == 1:
                a, b = path[1]
            else:
                a *= -1
                b *= -1
            p += 1
        elif loc == 4:
            if a == 1 and b == 0:
                a, b = path[2]
            elif a == 0 and b == 1:
                a, b = path[0]
            else:
                a *= -1
                b *= -1
            p += 1
        elif loc == 5:
            a *= -1
            b *= -1
            p += 1
        elif loc > 5:
            for w in wh[loc]:
                if w != [y, x]:
                    if 0 <= w[0] + a < N and 0 <= w[1] + b < N:
                        y, x = w
                    else:
                        a *= -1
                        b *= -1
                        p += 1
                    break
        if 0 > y + a or y + a == N or 0 > x + b or x + b == N:
            a = -a1
            b = -b1
            p += 1
        y += a
        x += b


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
    ans = 0
    for row in range(N):
        for col in range(N):
            if pan[row][col] == 0:
                for a, b in path:
                    if pan[row][col] == 0:
                        play(row+a, col+b, a, b, 0)
    print('#{} {}'.format(tc, ans))
