N = int(input())
n = int(N**0.5)
ans = 0
while N:
    cal = N // n**2
    if cal > 0:
        N -= n**2 * cal
        ans += cal
    n -= 1
print(ans)
