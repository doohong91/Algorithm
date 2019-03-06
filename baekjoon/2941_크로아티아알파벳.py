word = input()
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
trans = []
i = 0
while i < len(word):
    if word[i:i+3] in cro:
        trans.append(word[i:i+3])
        i += 3
    elif word[i:i+2] in cro:
        trans.append(word[i:i+2])
        i += 2
    else:
        trans.append(word[i])
        i += 1
print(len(trans))