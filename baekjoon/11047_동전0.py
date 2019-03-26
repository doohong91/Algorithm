N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
cnt = 0
for a in A[::-1]:
    if K // a:
        cnt += K // a
        K = K % a
print(cnt)