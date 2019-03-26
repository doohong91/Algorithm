def dfs(v):
    vis[v] += 1
    print(v, end=' ')
    for w in G[v]:
        if not vis[w]:
            bfs(w)


def bfs(v):
    que = [v]
    vis[v] += 1
    while que:
        v = que.pop(0)
        print(v, end=' ')
        for w in G[v]:
            if not vis[w]:
                que.append(w)
                vis[w] += 1


N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
    n1, n2 = map(int, input().split())
    G[n1].append(n2)
    G[n2].append(n1)
for i in range(N+1):
    print(G[i])
    G[i] = sorted(G[i])
    print(G[i])
vis = [0]*(N+1)
dfs(V)
print()
vis = [0]*(N+1)
bfs(V)
