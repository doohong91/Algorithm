n = int(input())
w = [0]*1002
loc = [0]*(n+1)
for i in range(n):
    l,h = map(int,input().split())
    w[l] = h
    loc[i] = l
loc[-1] = 1001
loc = sorted(loc)
result = max_j1 = max_j2 = max_i = j = 0
while j < n:
    i = loc[j]
    if w[i] > w[max_i]:
        result += (i-max_i)*w[max_i]
        max_i = i
        max_j1 = j
    j += 1
max_i = 0
while j >= max_j1:
    i = loc[j]
    if w[i] > w[max_i]:
        result += (max_i-i)*w[max_i]
        max_i = i
        max_j2 = j
    j -= 1 
result += (max_j2-max_j1+1)*w[max_i]
print(result)