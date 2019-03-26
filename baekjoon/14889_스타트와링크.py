from itertools import combinations

N = int(input())
ca = [list(map(int, input().split())) for _ in range(N)]
member = list(range(1, N+1))
comb = list(combinations(member, N//2))
done = {team: 1 for team in comb}
i = 0
result = 100 * (N//2)
while i < len(done) and done[comb[i]]:
    team = [comb[i], 0]
    team[1] = tuple(n for n in member if n not in team[0])
    score = [0] * 2
    ans = 0
    for j in range(2):
        for p in team[j]:
            for c in team[j]:
                score[j] += ca[p-1][c-1]
        done[team[j]] = 0
    ans = abs(score[0] - score[1])
    if ans < result:
        result = ans
    i += 1
print(result)