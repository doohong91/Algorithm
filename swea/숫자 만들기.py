def backtrack(k, cal, O):
    global N, min_c, max_c
    if k == N-1:
        if cal < min_c:
            min_c = cal
        if cal > max_c:
            max_c = cal
        return
    else:
        for c in range(4):
            op = O[::]
            if op[c]:
                op[c] -= 1
                if c == 0:
                    backtrack(k + 1, cal + nums[k + 1], op)
                elif c == 1:
                    backtrack(k + 1, cal - nums[k + 1], op)
                elif c == 2:
                    backtrack(k + 1, cal * nums[k + 1], op)
                elif c == 3:
                    backtrack(k + 1, int(cal / nums[k + 1]), op)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    min_c = 100000001
    max_c = -100000001
    backtrack(0, nums[0], P)
    ans = max_c - min_c
    print(f'#{tc} {ans}')
