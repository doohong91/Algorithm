def powerset(d, sums):
    global n_chu, n_ball
    if sums < 0:
        sums *= -1
        if sums in cand:
            return
    if sums not in cand:
        cand.append(sums)
    if sums in ball:
        for i in range(n_ball):
            if ball[i] == sums:
                found[i] = 1
        return
    if d == n_chu:
        return
    if sum(found) < n_ball:
        powerset(d + 1, sums + chu[d])
    if sum(found) < n_ball:
        powerset(d + 1, sums)
    if sum(found) < n_ball:
        powerset(d + 1, sums - chu[d])

n_chu = int(input())
chu = list(map(int,input().split()))
n_ball = int(input())
ball = list(map(int,input().split()))
found = [0]*n_ball
cand = []
powerset(0,0)
for f in found:
    if f:
        print('Y', end=' ')
    else:
        print('N', end=' ')