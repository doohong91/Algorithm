path = [(0, 1), (-1, 0), (0, -1), (1, 0)]
path2 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def spread():
    area_sub = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if area[r][c] > 0:
                cnt = 0
                for pr, pc in path:
                    if 0 <= r + pr < R and 0 <= c + pc < C and area[r + pr][c + pc] != -1:
                        area_sub[r + pr][c + pc] += area[r][c]//5
                        cnt += 1
                area[r][c] -= cnt * (area[r][c]//5)
    merge_area(area, area_sub)

def merge_area(area1, area2):
    for r in range(R):
        for c in range(C):
            area1[r][c] += area2[r][c]

def clear_area(ar, ac, path, lim):
    area_sub = [[0]*C for _ in range(R)]
    i = 0
    r, c = ar + path[i][0], ac + path[i][1]
    while (r, c) != (ar, ac):
        now = area[r][c]
        area[r][c] = 0
        if lim[0] <= r + path[i][0] < lim[1] and 0 <= c + path[i][1] < C:
            r, c = r + path[i][0], c + path[i][1]
            area_sub[r][c] = now
        else:
            i += 1
            r, c = r + path[i][0], c + path[i][1]
            area_sub[r][c] = now
    replace_area(area, area_sub)

def replace_area(area1, area2):
    for r in range(R):
        for c in range(C):
            if area[r][c] >= 0 and area2[r][c] > 0 and area1[r][c] != area2[r][c]:
                area1[r][c] = area2[r][c]

def cal_dust():
    cal = 2
    for r in range(R):
        for c in range(C):
            cal += area[r][c]
    return cal

R, C, T = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(R)]

for ar in range(R):
    if -1 in area[ar]:
        ac = area[ar].index(-1)
        break

for _ in range(T):
    spread()
    clear_area(ar, ac, path, [0, ar + 1])
    clear_area(ar + 1, ac, path2, [ar + 1, R])

ans = cal_dust()
print(ans)
