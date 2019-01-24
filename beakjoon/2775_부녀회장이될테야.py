testcase = int(input())
for t in range(testcase):
    k = int(input())
    n = int(input())
    apt = [list(range(n+1)) for x in range(k+1)]
    for f in range(1,k+1):
        for r in range(n+1):
            apt[f][r] = sum(apt[f-1][:r+1])
    print(apt[k][n])