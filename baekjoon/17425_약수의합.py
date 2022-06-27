
import sys

arr = [1] * 1000001
result = [0] * 1000001
result[1] = 1
for i in range(2, 1000001):
    j = 1
    while i * j < 1000001:
        arr[i*j] += i
        j += 1
    
    result[i] = result[i-1] + arr[i]

T = int(input())

for _ in range(T):
    a = int(sys.stdin.readline())
    sys.stdout.write(str(result[a])+"\n")