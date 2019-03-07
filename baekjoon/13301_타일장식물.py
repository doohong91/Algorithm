def cal(t,v):
    global N
    result.append(v)
    if t == N:   
        return
    cal(t+1,result[t-1]+result[t-2])
    
N = int(input())
result = [1,1]
if N > 2:
    cal(3,2)
    ans = result[-1]*2+(result[-2]+result[-1])*2
else:
    ans = 1*2 + 1*N*2
print(ans)