num = input()
counts = [0]*10
for n in num:
    counts[int(n)] += 1
result = ''
for i in range(9,-1,-1):
    result += str(i)*counts[i]
print(int(result))