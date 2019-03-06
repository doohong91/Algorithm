word = input().upper()
di={}
for s in word:
    try:
        di[s] += 1
    except:
        di[s] = 1
g = 0
result = ''
for k,v in di.items():
    if v > g:
        g = v
        result = k
    elif v == g:
        result = '?'
print(result)