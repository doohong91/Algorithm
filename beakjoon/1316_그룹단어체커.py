t = int(input())
for i in range(t):
    s = input()
    cnt = 0
    if len(s) == 1:
        cnt += 1
    for c in s:
        s.indexes(c)
            
        elif s[i] == s[i-1] and s[i] in s[:i-1]:
            break
    print(s)
    cnt += 1
print(cnt)