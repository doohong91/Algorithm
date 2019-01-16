t = int(input())
for i in range(t):
    li = [i for i in input().split('X') if i]
    score = 0
    for l in li:
        n = len(l)
        score += int(n*(n+1)/2)
    print(score)