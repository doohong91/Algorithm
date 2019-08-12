N = int(input())
A = list(map(int, input().split()))
cals = [0]*N
cals[0] = A[0]
for i in range(1, N):
    cals[i] = A[i]
    m = i
    for j in range(i-1, -1, -1):
        if A[j] < A[m]:
            cals[i] += A[j]
            m = j
print(max(cals))
