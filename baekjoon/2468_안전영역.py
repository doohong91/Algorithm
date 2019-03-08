N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
path = [(0, -1), (0, 1), (-1, 0), (1, 0)]
result = 0
h = 0
while h < 101:
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    save = area[0][0]
    eq = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] == save:
                eq += 1
            if area[i][j] > h and not visited[i][j]:
                cnt += 1
                que = [(i, j)]
                while que:
                    r, c = que.pop(0)
                    visited[r][c] = 1
                    for p in path:
                        a, b = p
                        if 0 <= r + a < N and 0 <= c + b < N:
                            if area[r + a][c + b] > h and not visited[r + a][c + b]:
                                que.append((r + a, c + b))
            if eq == N ** 2 or e1 == N ** 2 - 1:
                break
        if eq == N ** 2 or e1 == N ** 2 - 1:
            break
    h += 1
    if eq == N ** 2:
        result = 1
        break
    elif e1 == N ** 2 - 1:
        result = 2
        break
    elif result < cnt:
        result = cnt
    elif result > cnt:
        break             
print(result)