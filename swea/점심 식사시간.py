T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = [0]*N
    S = []
    P = []
    for i in range(N):
        M[i] = list(map(int, input().split()))
        for j in range(N):
            if M[i][j] == 1:
                P.append([i, j])
            elif M[i][j] > 1:
                S.append([i, j, M[i][j]])
    S1 = []
    S2 = []
    for p in P:
        D = [0, 0]
        for i in range(2):
            D[i] = abs(S[i][0] - p[0]) + abs(S[i][1] - p[1])
        S1.append(D[0])
        S2.append(D[1])
    V = list(range(len(P)))
    w1 = []
    w2 = []
    x1 = S[0][2]
    x2 = S[1][2]
    while V:
        t1 = min(V, key=lambda x: S1[x])
        t2 = min(V, key=lambda x: S2[x])

        if len(w1) == 3 and S1[t1] < w1[0]:
            s1 = 2 * (S1[t1] + x1) - w1[0] + 1
        else:
            s1 = S1[t1] + x1 + 1

        if len(w2) == 3 and S2[t2] < w2[0]:
            s2 = 2 * (S2[t2] + x2) - w2[0] + 1
        else:
            s2 = S2[t2] + x2 + 1

        if s1 > s2:
            p = t2
            w2.append(s2)
        elif s1 < s2:
            p = t1
            w1.append(s1)
        else:
            if len(w1) > len(w2):
                p = t2
                w2.append(s2)
            elif len(w1) <= len(w2):
                p = t1
                w1.append(s1)
        if len(w1) == 4:
            w1.pop(0)
        if len(w2) == 4:
            w2.pop(0)
        V.remove(p)

    a = w1[-1] if w1 else 0
    b = w2[-1] if w2 else 0
    print('#{} {}'.format(tc, max(a, b)))