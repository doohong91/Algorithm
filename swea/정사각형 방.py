import sys
sys.stdin = open('input.txt', 'r')
import time
stime = time.time()
from collections import deque


def move(y, x, cnt):
    global N, ans, st, i, j
    que = deque([(y, x, cnt)])
    V[y][x] = 1
    while que:
        y, x, cnt = que.popleft()
        for py, px in path:
            if 0 <= y+py < N and 0 <= x+px < N and A[y][x] + 1 == A[y+py][x+px]:
                que.append((y+py, x+px, cnt + 1))
                V[y+py][x+px] = 1
    if cnt >= ans:
        if cnt > ans:
            st = deque([])
        ans = cnt
        st.append(A[i][j])


path = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    V = [[0]*N for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if V[i][j] == 0:
                move(i, j, 1)
    print('#{} {} {}'.format(tc, min(st), ans))

print(time.time() - stime)
