T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if len(A) < len(B):
        L = B
        S = A
    else:
        L = A
        S = B
    result = 0
    for k in range(len(L)-len(S)+1):
        cal = 0
        for i in range(len(S)):
            cal += L[k+i]*S[i]
        if cal > result:
            result = cal
    print('#{} {}'.format(tc, result))