N = int(input())
array = list(map(int,input().split()))
cnt = 0
for num in array:
    if num > 1:
        for a in range(2,num):
            if not num%a:
                num = 0
                break
        if num:        
            cnt += 1
print(f'{cnt}')