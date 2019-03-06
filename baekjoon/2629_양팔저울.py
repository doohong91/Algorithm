def powerset(d, sums):
    global n_chu, b, found
    if sums == b:
        found = 1
        return
    if not found:
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
for b in ball:
    found = 0
    powerset(0,0)
    if found:
        print('Y', end=' ')
    else:
        print('N', end=' ')