li = [int(i) for i in input().split()]
if li == sorted(li):
    print('ascending')
elif li[::-1] == sorted(li):
    print('descending')
else:
    print('mixed')