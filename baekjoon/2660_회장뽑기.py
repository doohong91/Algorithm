n = int(input())
mem = [[] for _ in range(n+1)]
cand = []
ans = n
while 1:
    f1,f2 = map(int,input().split())
    if f1 == -1 and f2 == -1:
        break
    mem[f1].append(f2)
    mem[f2].append(f1)
for no in range(1,n+1):
    visited = [no]
    score = 1
    que = []
    for f in mem[no]:
        if f not in visited:
            que.append((f,score))
            visited.append(f)
    while que:
        fr, sc = que.pop(0)
        for f in mem[fr]:
            if f not in visited:
                que.append((f,sc+1))
                visited.append(f)
        if sc > score:
            score = sc
    if ans > score:
        cand = [no]
        ans = score
    elif ans == score:
        cand.append(no)
print('{} {}'.format(ans,len(cand)))
for c in cand:
    print(c, end=' ')