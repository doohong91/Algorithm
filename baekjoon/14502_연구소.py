import itertools
import copy

path = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_virus(N, M):
    for row in range(N):
        for col in range(M):
            if area[row][col] == 2:
                virus.append((row, col))

def infection(area, N, M):
    global ans
    for row, col in virus:
        que = [(row,col)]
        while que:
            r,c = que.pop()
            for pr, pc in path:
                if 0 <= r + pr < N and 0 <= c + pc < M and area[r+pr][c+pc] == 0:
                    area[r+pr][c+pc] = 2
                    que.append((r+pr, c+pc))
    safe = len(find_safe(area, N, M))
    if ans < safe:
        ans = safe
            
def find_safe(area, N, M):
    cnt = []
    for row in range(N):
        for col in range(M):
            if area[row][col] == 0:
                cnt.append((row, col))
    return cnt

N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
virus = []
find_virus(N, M)
ans = 0
safe_area = find_safe(area, N, M)
for walls in itertools.combinations(safe_area, 3):
    area_ = copy.deepcopy(area)
    for wr, wc in walls:
        area_[wr][wc] = 1
    infection(area_, N, M)
print(ans)