testcase = int(input())
for t in range(testcase):
    h,w,n = map(int, input().split())
    room = (n-1)//h + 1
    floor = h if n%h == 0 else n%h
    print(f'{floor}{room:02d}')