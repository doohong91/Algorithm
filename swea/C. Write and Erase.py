T = int(input())
for tc in range(1,T+1):
    N = int(input())
    result = []
    for _ in range(N):
        A = input()
        if A in result:
            result.remove(A)
        else:
            result.append(A)
    print('#{} {}'.format(tc, len(result)))