def backtrack(k, cal):
    global ans
    if k >= len(use) and cal < ans:
        ans = cal
    elif k < len(use) and cal < ans:
        backtrack(k+1, cal + cost[0]*plan[use[k]])
        backtrack(k+1, cal + cost[1])
        backtrack(k+3, cal + cost[2])

T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    use = [i for i in range(12) if plan[i]]
    ans = cost[3]
    backtrack(0, 0)
    print(f'#{tc} {ans}')
