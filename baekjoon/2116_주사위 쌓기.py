n = int(input())
dices = [list(map(int,input().split())) for _ in range(n)]
result = i = 0
while i < 6:
    j = i
    res = 0
    dk = -1
    for d in range(n):
        max_d = 0
        for di in range(6):
            if dices[d][di] == dk:
                j = di
        if j == 0:
            k = 5
        if j == 5:
            k = 0
        else:
            if j > 2:
                k = j - 2
            else:
                k = j + 2
        dk = dices[d][k]
        for idx in range(6):
            if (idx != j or idx != k) and dices[d][idx] > max_d:
                max_d = dices[d][idx]
        res += max_d
    i += 1
    if res > result:
        result = res
print(result)
