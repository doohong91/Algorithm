n = int(input())
N = int(input())
link = [[] for _ in range(n+1)]
for _ in range(N):
    s,e = map(int,input().split())
    link[s].append(e)
    link[e].append(s)
visited = [0]*(n+1)
que = [1]
visited[1] = 1
while que:
    com = que.pop(0)
    for l in link[com]:
        if not visited[l]:
            que.append(l)
            visited[l] = 1
print(sum(visited)-1)