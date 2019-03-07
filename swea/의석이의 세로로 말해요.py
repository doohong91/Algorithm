T = int(input())
for tc in range(1,T+1):
    words = [[-1]*15 for _ in range(5)]
    for i in range(5):
        word = [s for s in input()]
        for j in range(len(word)):
            words[i][j] = word[j]
    result = ''
    for j in range(15):
        for i in range(5):
            if words[i][j] != -1:
                result += words[i][j]
    print('#{} {}'.format(tc, result))