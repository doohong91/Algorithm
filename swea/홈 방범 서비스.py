import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = [0]*N
    H = []
    for i in range(N):
        A[i] = list(map(int, input().split()))
        for j in A[i]:
            if j:
                H.append([i, j])


    print('#{} {}'.format(tc, k))
