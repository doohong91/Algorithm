N, M = map(int,input().split())
ice = [list(map(int,input().split())) for _ in range(N)]
path = [(-1,0),(1,0),(0,-1),(0,1)]
year = 0
while 1:
    cnt = sums = 0
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ice[i][j] and not visited[i][j]:
                cnt += 1
                if cnt > 1: break
                visited[i][j] = 1
                que = [(i,j)]
                stack = []
                while que:
                    r,c = que.pop(0)
                    cost = 0
                    for p in path:
                        a,b = p
                        if 0 <= r+a < N and 0 <= c+b < M:
                            if not ice[r+a][c+b]:
                                cost += 1
                            elif ice[r+a][c+b] and not visited[r+a][c+b]:
                                que.append((r+a,c+b))
                                visited[r+a][c+b] = 1
                    stack.append((r,c,cost))
                while stack:
                    r,c,sea = stack.pop()
                    if ice[r][c] > sea:
                        ice[r][c] -= sea
                    else: ice[r][c] = 0
                    sums += ice[r][c]
        if cnt > 1: break
    if cnt > 1: break
    if not sums: 
        year = 0
        break
    year += 1
print(year)