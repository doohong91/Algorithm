import sys
sys.stdin = open('input.txt', 'r')

path = [(-1, 0), (1, 0), (0, -1), (0, 1)]
shape = {
    1: [0, 1, 2, 3], 2: [0, 1], 3: [2, 3], 4: [0, 3],
    5: [1, 3], 6: [1, 2], 7: [0, 2], 0: []
}
togo = {
    0: [1, 2, 5, 6], 1: [1, 2, 4, 7], 2: [1, 3, 4, 5], 3: [1, 3, 6, 7]
}
T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    V = [[0]*M for _ in range(N)]
    que = [(R, C, L - 1)]
    V[R][C] = 1
    ans = 1
    while que:
        y, x, time = que.pop(0)
        if time == 0:
            break
        for i in shape[B[y][x]]:
            py, px = path[i]
            if 0 <= y + py < N and 0 <= x + px < M:
                if B[y + py][x + px] in togo[i] and V[y + py][x + px] == 0:
                    que.append((y + py, x + px, time - 1))
                    V[y + py][x + px] = 1
                    ans += 1
    print('#{} {}'.format(tc, ans))