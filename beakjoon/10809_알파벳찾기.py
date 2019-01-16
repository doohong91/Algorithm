import string
s = input()
alpha = list(string.ascii_lowercase)
li = []
for a in alpha:
    if a not in s:
        li.append(-1)
    else :
        li.append(s.index(a))
for l in li:
    print(l, end=' ')