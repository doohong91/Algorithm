path = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [[5]*N for _ in range(N)]
T = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    T[x-1][y-1].append(z)
while K:
    for r in range(N):
        for c in range(N):
            li = []
            dead = 0
            for tree in sorted(T[r][c]):
                if tree <= B[r][c]:
                    B[r][c] -= tree
                    li.append(tree + 1)
                else:
                    dead += tree // 2
            T[r][c] = li
            B[r][c] += dead + A[r][c]
    for r in range(N):
        for c in range(N):
            for tree in T[r][c]:
                if tree % 5 == 0:
                    for px, py in path:
                        if 0 <= r + py < N and 0 <= c + px < N:
                            T[r + py][c + px].append(1)
    K -= 1
ans = 0
for r in range(N):
    for c in range(N):
        ans += len(T[r][c])
print(ans)