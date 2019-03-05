n = int(input())
switch = list(map(int,input().split()))
p = int(input())
for _ in range(p):
    gen, num = map(int,input().split())
    if gen == 1:
        for i in range(num-1,n,num):
            if switch[i]:
                switch[i] = 0
            else: 
                switch[i] = 1
    else:
        i = 1
        num -= 1
        if switch[num]:
            switch[num] = 0
        else: 
            switch[num] = 1
        while num-i >= 0 and n > num+i:
            if switch[num-i] != switch[num+i]:
                break
            else:
                if switch[num-i]:
                    switch[num-i] = 0
                    switch[num+i] = 0
                else:
                    switch[num-i] = 1
                    switch[num+i] = 1
            i += 1
cnt = 0
for s in switch:
    if cnt == 20:
        print()
        cnt = 0
    print(s, end=' ')
    cnt += 1