a = int(input())
b = int(input())
c = int(input())
r = str(a*b*c)
li = [0]*10
for i in r:
   li[int(i)] += 1 
for l in li:
    print(l)