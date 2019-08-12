N = int(input())
A = list(map(int, input().split()))
cals = [0]*N
cals[-1] = A[-1]
for n in range(N-2, -1, -1):
    for i in range(n, N):
        if A[n] < A[i] and cals[n] < cals[i]:
            cals[n] = cals[i]
    cals[n] += A[n]
    
print(max(cals))

print(cals)