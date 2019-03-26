N = int(input())
que = list(range(1, 10))
if N < 9:
    print(N)
elif N > 1022:
    print(-1)
else:
    N -= 9
    while N > 0:
        num = que.pop(0)
        for i in range(10):
            if num == 0 or i < num % 10:
                que.append(num * 10 + i)
                N -= 1
    print(que[N-1])