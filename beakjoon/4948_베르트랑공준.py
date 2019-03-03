while 1:
    n = int(input())
    if not n:
        break
    cnt = 0
    for num in range(n+1,2*n+1):
        if num == 2 or num == 5:
            cnt += 1
        elif num % 10 in [1,3,7,9] and num > 1:
            for s in range(3,int(num**0.5)+1,2):
                if not num % s:
                    num = 0
                    break
            if num:
                cnt += 1
    print(f'{cnt}')