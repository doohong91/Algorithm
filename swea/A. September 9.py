T = int(input())
for tc in range(1,T+1):
    N = input()
    print('#{} {}'.format(tc, 'Yes' if '9' in N else 'No'))