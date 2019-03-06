dial = [[],['a','b','c'],['d','e','f'],['g','h','i'],
['j','k','l'],['m','n','o'],['p','q','r','s'],
['t','u','v'],['w','x','y','z']]
s = input().lower()
time = 0
for c in s:
    for i in range(len(dial)):
        if c in dial[i]:
            time += (i+2)
print(time)