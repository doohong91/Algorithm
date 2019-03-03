T = int(input())
for tc in range(T):
    n = int(input())
    sosu = []
    for num in range(n//2,1,-1):
        if num == 2 or num == 5:
            sosu.append(num)
        elif num % 10 in [1,3,7,9] and num > 1:
            for s in range(3,int(num**0.5)+1,2):
                if not num % s:
                    num = 0
                    break
            if num:
                sosu.append(num)
    for ss in sosu:
        num = n - ss
        for s in range(3,int(num**0.5)+1,2):
            if not num % s:
                num = 0
                break
        if num:
            result = f'{ss} {num}'
            break
    print(result)