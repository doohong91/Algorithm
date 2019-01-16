import math
a = ['  *  ',' * * ','*****']
def star(n):
    c = len(a)
    s = ' '
    for i in range(c):
        a.append(a[i] + s + a[i])
        a[i] = s*3*n + a[i] + s*3*n

n = int(input())
k = int(math.log(n/3,2))
for i in range(k):
    star(2**i)
for r in range(n):
    print(a[r])