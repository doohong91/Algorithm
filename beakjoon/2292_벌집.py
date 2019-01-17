cnt = 0
import sys
n = int(sys.stdin.readline())
sums = 0
while n > sums:
    sums += 6*cnt
    cnt += 1
    if n <= 1+sums:
        break
print(cnt)