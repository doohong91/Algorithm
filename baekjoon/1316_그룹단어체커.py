n = int(input())
cnt = 0
for t in range(n):
    s = input()
    ok = True
    for c in s:
        li = [i for i,v in enumerate(s) if v == c]
        if list(range(li[0],li[0] + len(li))) != li:
            ok = False
            break
    if ok == True:
        cnt += 1
print(cnt)