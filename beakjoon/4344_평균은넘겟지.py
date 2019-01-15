# c = int(input())
c = 1
for i in range(c):
    li = [int(i) for i in input().split()]
    n = li.pop(0)
    mu = sum(li)/n
    print(f'{len([i for i in li if i > mu])/n*100:.3f}%')