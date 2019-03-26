N = int(input())
tt = [list(map(int, input().split())) for _ in range(N)]
tt = sorted(tt, key=lambda x: (x[0], x[1]), reverse=True)
i = result = 1
st = tt[0][0]
while i < N:
    if st >= tt[i][1]:
        result += 1
        st = tt[i][0]
    i += 1
print(result)