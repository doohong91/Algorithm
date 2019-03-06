k = int(input())
x = [0]*3
y = [0]*3
for _ in range(6):
    dr,ds = map(int,input())
    if dr == 1 :
        x += ds
    if dr == 2:
        x -= ds
    if dr == 3:
        y -= ds
    if dr == 4:
        y += ds
