def self_number(num):
    s1 = set(n + sum([int(i) for i in str(n)]) for n in range(1,num+1))
    s2 = set(range(1,num+1))
    return sorted(list(s2 - s1))

li = self_number(10000)
for i in li:
    print(i)

