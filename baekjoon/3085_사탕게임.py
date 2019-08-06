from copy import deepcopy
C = ["C", "P", "Z", "Y"]
N = int(input())
ans = 0
B = [[c for c in input()] for _ in range(N)]

for i in range(N):
    for n in range(ans+1, N+1):
        notfound = 0
        for c in C:
            if c*n in ''.join(B[i]):
                ans = n
            elif c*n in ''.join([B[t][i] for t in range(N)]):
                ans = n
            else:
                notfound += 1
        if notfound == 4:
            break

for i in range(N):
    for j in range(N-1):
        if B[i][j] != B[i][j+1]:
            pan = deepcopy(B)
            pan[i][j], pan[i][j+1] = pan[i][j+1], pan[i][j]
            for n in range(ans+1, N+1):
                notfound = 0
                for c in C:
                    if c*n in ''.join(pan[i]):
                        ans = n
                    elif c*n in ''.join([pan[t][j] for t in range(N)]):
                        ans = n
                    elif c*n in ''.join([pan[t][j+1] for t in range(N)]):
                        ans = n
                    else:
                        notfound += 1
                if notfound == 4:
                    break

for i in range(N-1):
    for j in range(N):
        if B[i][j] != B[i+1][j]:
            pan = deepcopy(B)
            pan[i][j], pan[i+1][j] = pan[i+1][j], pan[i][j]
            for n in range(ans+1, N+1):
                notfound = 0
                for c in C:
                    if c*n in ''.join(pan[i]):
                        ans = n
                    elif c*n in ''.join(pan[i+1]):
                        ans = n
                    elif c*n in ''.join([pan[t][j] for t in range(N)]):
                        ans = n
                    else:
                        notfound += 1
                if notfound == 4:
                    break

print(ans)
