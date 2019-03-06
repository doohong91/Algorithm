numb = int(input())
for z in range(numb):
    m, n, k, l = map(int,input().split())
    if m < k or n < l:
        l = -1
        print(l)
        continue
    if m < n:
        m,n = n,m
        k,l = l,k
    res = n    
    while res%m != 0:
        res += n
    while l<=res :
        if l % m ==(k%m):
            break
        l+=n
    if l > res:
        l = -1
    print(l)