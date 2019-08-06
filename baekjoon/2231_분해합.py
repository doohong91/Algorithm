M = input()
m = len(M)
M = int(M)
ans = 0
min_N = M - 9*m if M > 9*m else 0

for N in range(min_N, M + 1):
    cal = N
    NN = str(N)
    for i in range(len(NN)):
        cal += int(NN[i])
    if cal == M:
        ans = N
        break

print(ans)
