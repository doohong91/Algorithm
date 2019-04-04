import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    w1 = []
    w2 = []


    print('#{} {}'.format(tc, k))
