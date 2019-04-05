from itertools import combinations, product


def pass_check(F):
    global W, D, K
    for c in range(W):
        cnt = ok = 0
        b = F[0][c]
        for r in range(1, D):
            if F[r][c] == b:
                cnt += 1
                if cnt == K - 1:
                    ok = 1
                    break
            else:
                cnt = 0
                b = F[r][c]
        if ok == 0:
            return False
    return True


def drug(ans):
    global D, W, K
    while ans < K:
        case = [i for i in product(['0', '1'], repeat=ans)]
        for row in combinations(range(D), ans):
            for smp in case:
                test = film[::]
                for i in range(ans):
                    test[row[i]] = [smp[i]] * W
                ok = pass_check(test)
                if ok:
                    return ans
        ans += 1
    return ans


T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    film = [list(input().split()) for _ in range(D)]
    ok = pass_check(film)
    ans = 0
    if not ok:
        ans = drug(ans + 1)
    if K == 1:
        ans = 0
    print('#{} {}'.format(tc, ans))