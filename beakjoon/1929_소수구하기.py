M, N = map(int,input().split())
for num in range(M,N+1):
    if num == 2 or num == 5:
        print(f'{num}')
    elif num % 10 in [1,3,7,9] and num > 1:
        for a in range(3,int(num**(1/2))+1,2):
            if not num % a:
                num = 0
                break
        if num:
            print(f'{num}')