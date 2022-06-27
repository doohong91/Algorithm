A, B = list(map(int, input().split()))

set_a = [1]

for i in range(2, max(A, B) + 1):
    if A % i == 0 and B % i == 0:
        set_a.append(i)

print(set_a[-1])
print(A * B // set_a[-1])
