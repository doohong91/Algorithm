a = input()
for i in range(0,len(a),10):
    if i+10 > len(a):
        print(a[i:])
    else:
        print(a[i:i+10])