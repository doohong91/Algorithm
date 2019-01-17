n = int(input())
li = []
a = b = 1
sums = 0
cnt = 1
while sums <= n:
    if cnt % 2 == 1:
        b=1
        for i in range(cnt):
            li.append(f'{a}/{b}')
            a -= 1
            b += 1
    else :
        a=1
        for i in range(cnt):
            li.append(f'{a}/{b}')
            b -= 1
            a += 1
    sums += cnt
    cnt += 1
print(li[n-1])