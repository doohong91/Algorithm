def powerset(d, sums):
    global n_chu, n_ball
    if sums in ball:
        for i in range(n_ball):
            if ball[i] == sums:
                found[i] = 1
        return
    if sum(found) < n_ball:
        if d == n_chu:
            return
        for i in range(3): 
            if i:
                if i == 1:
                    powerset(d+1, sums+chu[d])
                else:
                    powerset(d+1, sums-chu[d])
            else:
                powerset(d+1, sums)
          
n_chu = int(input())
chu = list(map(int,input().split()))
n_ball = int(input())
ball = list(map(int,input().split()))
cand = [0,1,2]
used = [0]*n_chu
found = [0]*n_ball
powerset(0,0)
for f in found:
    if f:
        print('Y', end=' ')
    else:
        print('N', end=' ')