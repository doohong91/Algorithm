T = int(input())
for tc in range(1,T+1):
    N = int(input())
    result = ''
    for _ in range(N):
        ci, ki = input().split()
        result += ci*int(ki)
    print('#{}'.format(tc))
    for i in range(len(result)):
        print(result[i], end='')
        if (i+1) % 10 == 0:
            print()
    print()