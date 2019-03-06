t = int(input())
for i in range(t):
    r, s = input().split()
    r = int(r)
    result = ''
    for c in s:
        result += c*r
    print(result)