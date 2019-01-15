def hansoo(num):
    if num < 100:
        return True
    else : 
        l1 = [int(i) for i in str(num)]
        s1 = set(l1[i+1] - l1[i] for i in range(len(l1)-1))
        return len(s1) == 1

n = int(input())
li = [i for i in range(1,n) if hansoo(i)]
print(len(li))
