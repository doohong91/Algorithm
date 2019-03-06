N = int(input())
M = [[int(n) for n in input()] for _ in range(N)]
result = []
for i in range(N):
    for j in range(N):
        if M[i][j]:
            li = []
            cnt = 0
            li.append((i,j))
            while li:
                r,c = li.pop()
                if M[r][c]:
                    M[r][c] = 0
                    cnt += 1
                    for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                        if 0 <= r+x < N and 0 <= c+y < N:
                            li.append((r+x,c+y))
            result.append(cnt)
result = sorted(result)
print(len(result))
for r in result:
    print(r)