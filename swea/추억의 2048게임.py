T = int(input())
for tc in range(1, T+1):
    N, S = input().split()
    N = int(N)
    T = [list(map(int, input().split())) for _ in range(N)]
    path = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
    done = [[0]*N for _ in range(N)]
    if S == 'down':
        case1 = (N - 1, -1, -1)
        case2 = (0, N, 1)
    elif S == 'right':
        case1 = (0, N, 1)
        case2 = (N-1, -1, -1)
    else:
        case1 = (0, N, 1)
        case2 = (0, N, 1)
    for i in range(*case1):
        for j in range(*case2):
            if T[i][j]:
                a, b = path[S]
                que = [(i, j)]
                while que:
                    r, c = que.pop(0)
                    if 0 <= r + a < N and 0 <= c + b < N:
                        if (T[r + a][c + b] == T[r][c] and not done[r + a][c + b] and not done[r][c]) or T[r + a][c + b] == 0:
                            if T[r + a][c + b]:
                                done[r + a][c + b] = 1
                            T[r + a][c + b] += T[r][c]
                            T[r][c] = 0
                            que.append((r + a, c + b))
    print('#%d' % tc)
    for i in range(N):
        for j in range(N):
            print(T[i][j], end=' ')
        print()