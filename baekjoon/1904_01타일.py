N = int(input())
ans = [0]*N
ans[0] = 1
ans[1] = 2
for i in range(2, N):
    ans[i] = ((ans[i - 1] % 15746) + (ans[i-2] % 15746)) % 15746

print(ans[N-1])
