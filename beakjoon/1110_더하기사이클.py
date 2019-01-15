n = input()
li = [int(i) for i in n]
if len(n)==1:
    a, b = 0, li[0]
else:
    a,b= li
count = 0
while 1:
    count += 1
    c = a+b
    if b*10 + c%10 == int(n):
        break
    else:
        a = b
        b = c%10
print(count)
