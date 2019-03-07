def powerset(d,sums,cnt):
    global max_s
    if cnt == 3:
        if max_s < sums%10:
            max_s = sums%10
        return
    elif d == 5:
        return
    for c in cand:
        if c:
            visited[d] = 1
            powerset(d+1,sums+cards[d],cnt+1)
        else:
            powerset(d+1,sums,cnt)

N = int(input())
cand = [0,1]
result = ans = 0
for i in range(1,N+1):
    cards = list(map(int,input().split()))
    visited = [0]*5
    max_s = 0
    powerset(0,0,0)
    if max_s >= result:
        result = max_s
        ans = i
    print(max_s)
print(ans)