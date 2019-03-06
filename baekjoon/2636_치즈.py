row, col = map(int, input().split())
C = [list(map(int,input().split())) for _ in range(row)]
found = 1
time = left = rr = cc = 0
move = [(0,0)]
while found:
    cnt = 0
    starts = []
    while move:
        i,j = move.pop()
        if C[i][j] == time*2 or not C[i][j]:
            C[i][j] = -1
            li = []
            for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                if 0 <= i+x < row and 0 <= j+y < col:
                    li.append((i+x,j+y))
            while li:
                r,c = li.pop(0)
                if C[r][c] == 1:
                    C[r][c] = (time+1)*2
                    cnt += 1
                    starts.append((r,c))
                elif C[r][c] == time*2 or not C[r][c]:
                    move.append((r,c))
    move = starts
    time += 1
    if cnt == 0:
        found = 0
    else: left = cnt
print(time-1)
print(left)