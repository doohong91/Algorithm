def is_danjo(num):
    i = '0'
    for n in str(num):
        if ord(n) < ord(i):
            return
        i = n
    return True

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    A = list(map(int,input().split()))
    result = -1
    for i in range(N-1):
        for j in range(i+1,N):
            if is_danjo(A[i]*A[j]) and A[i]*A[j]>result:
                result = A[i]*A[j]
    print('#{} {}'.format(tc, result))