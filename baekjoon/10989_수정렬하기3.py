import sys

N = int(input())
counts = [0]*10001

for i in range(N):
    counts[int(sys.stdin.readline())] += 1

for i in range(len(counts)):
    for n in range(counts[i]):
        print(i)