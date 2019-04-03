def combination(C, n, num):
    global ans
    if n == 0 and num > ans:
        ans = num
        return
    elif n > 0:
        D.append(num)
        for i in range(len(C)-1):
            for j in range(i+1, len(C)):
                P = C[::]
                P[i], P[j] = P[j], P[i]
                cal = int("".join(P))
                if cal not in D:
                    combination(P, n-1, cal)


T = int(input())
for tc in range(1, T + 1):
    card, N = input().split()
    N = int(N)
    cards = [c for c in card]
    ans = int(card)
    D = [ans]
    combination(cards, N, ans)
    print(f'#{tc} {ans}')
