def move(n, y, x, num):
    if n == 0 and num not in D:
        D.append(num)
        return
    elif n > 0:
        for a, b in path:
            if 0 <= y+b < 4 and 0 <= x+a < 4:
                move(n-1, y+b, x+a, num+M[y+b][x+a])


path = [(-1, 0), (1, 0), (0, -1), (0, 1)]
T = int(input())
for tc in range(1, T + 1):
    M = [list(input().split()) for i in range(4)]
    ans = ''
    D = []
    for i in range(4):
        for j in range(4):
            move(6, i, j, M[i][j])
    print(f'#{tc} {len(D)}')
