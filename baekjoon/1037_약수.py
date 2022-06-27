n = int(input())
arr = sorted(list(map(int, input().split())))

if n == 1:
    result = arr[0] ** 2
else:
    result = arr[0] * arr[-1]

print(result)