li = []
while 1:
    try:
        li.append(int(input()))
    except EOFError:
        break

print(sum(li))
