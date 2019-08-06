short = sorted([int(input()) for _ in range(9)])
cal = sum(short)
found = False

for i in range(8, 0, -1):
    for j in range(i, -1, -1):
        if cal - short[i] - short[j] == 100:
            found = True
            break
    if found:
        break

for n in range(9):
    if n not in [i, j]:
        print(short[n])
