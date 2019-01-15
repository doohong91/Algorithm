n = input()
li = [int(i) for i in input().split()]
li = [(i/max(li))*100 for i in li]
print(sum(li)/len(li))