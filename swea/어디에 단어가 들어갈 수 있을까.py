T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    puz = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    vis = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cnt = 0
            if puz[i][j] and not vis[i][j]:
                que = [(i,j)]
                while que:
                    r,c = que.pop(0)
                    vis[r][c] = 1
                    cnt += 1
                    if 0 <= c+1 < N and puz[r][c+1]:
                        que.append((r,c+1))
            if cnt == K:
                result += 1
    vis = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cnt = 0
            if puz[j][i] and not vis[j][i]:
                que = [(j, i)]
                while que:
                    r, c = que.pop(0)
                    vis[r][c] = 1
                    cnt += 1
                    if 0 <= r + 1 < N and puz[r+1][c]:
                        que.append((r+1,c))
            if cnt == K:
                result += 1
    print('#{} {}'.format(tc, result))