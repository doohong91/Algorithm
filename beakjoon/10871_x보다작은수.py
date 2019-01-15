# n, x = [int(i) for i in input().split()]
n, x = [10,5]
li = [i for i in input().split()]
print(' '.join(map(str,filter(lambda a : a < x, map(int, li)))).strip())