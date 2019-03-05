import sys
N = int(sys.stdin.readline())
result = []
for i in range(N//2+1):
    li = [N, N-2*i]
    while li[-2] - li[-1] >= 0:
        li.append(li[-2] - li[-1])
    if len(li) > len(result):
        result = li
print(len(result))
for n in result:
    print(n, end=' ')