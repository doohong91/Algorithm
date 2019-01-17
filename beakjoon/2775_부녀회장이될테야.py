testcase = int(input())
for t in range(testcase):
    k = int(input())
    n = int(input())
    zero = [p for p in range(1,n+1)]
    apt = []
    for r in range(n):
        room = [] #각 층의 r호
        for f in range(k):
            if f == 0: # 1층
                room.append(sum(zero[:r+1]))
                apt.append(room)
            else:
                room.append(sum(apt[f-1][:r+1]))
        apt.append(room)
    print(list(zip(*apt)))