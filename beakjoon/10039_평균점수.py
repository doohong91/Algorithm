li = []
for i in range(5):
    a = int(input())
    li.append(a if a>40 else 40)
print(int(sum(li)/len(li)))