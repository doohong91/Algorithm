T = int(input())
for tc in range(1,T+1):
    word = [w for w in input()]
    n = len(word)
    for i in range(5):
        if i == 2:
            line = '#.'
            for w in word:
                line += w+'.#.'
            line = line[:-1]
        elif i%2:
            line = '.'
            for _ in range(n):
                line += '#.#.'
        else:
            line = '.'
            for _ in range(n):
                line += '.#..'
        print(line)