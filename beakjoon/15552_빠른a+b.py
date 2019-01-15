import sys
t = int(sys.stdin.readline())
for i in range(t):
    print(sum([int(i) for i in sys.stdin.readline().split()]))