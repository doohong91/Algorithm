N = int(input())
if int(N**0.5)**2 == N:
    print(1)
else:
    dp = [0]*(N+1)
    for n in range(1, N+1):
        dp[n] = n
        for num in range(1, int(n**0.5)+1):
            if n >= num**2:
                dp[n] = min(dp[n], dp[n-num**2]+1)
            else:
                break
    print(dp[-1])
