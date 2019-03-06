N = int(input())
words = sorted(sorted(set([input() for _ in range(N)])),key=len)
for word in words:
    print(word)