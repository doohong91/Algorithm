N, K = map(int, input().split())
B = [[0]*(K+1) for _ in range(N+1)]
V = [0]*(N+1)
W = [0]*(N+1)
for i in range(N):
    W[i+1], V[i+1] = map(int, input().split())
for i in range(1, N+1):
    for j in range(1, K+1):
        if W[i] <= j:
            B[i][j] = max(B[i-1][j], V[i] + B[i-1][j-W[i]])
        else:
            B[i][j] = B[i-1][j]
for b in B:
    print(b)
print()
print(B[N][K])
