w,h = map(int,input().split())
paper = [[0]*(w+1) for _ in range(h+1)]
n = int(input())
width = height = 0
for _ in range(n):
    t, m = map(int, input().split())
    if t:
        for r in range(h+1):
            paper[r][m] = 1
    else:
        for c in range(w+1):
            paper[m][c] = 1
w_li = []
cnt = 0
for i in range(w):
    if paper[0][i]:
        w_li.append(cnt)
        cnt = 0
    cnt += 1 
w_li.append(cnt)
h_li = []
cnt = 0
for i in range(h):
    if paper[i][0]:
        h_li.append(cnt)
        cnt = 0
    cnt += 1 
h_li.append(cnt)
print(max(w_li)*max(h_li))