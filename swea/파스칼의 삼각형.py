T = int(input())
for tc in range(1,T+1):
    N = int(input())
    save = [0,1,0]
    print('#{}'.format(tc))
    for i in range(N):
        if i:
            line = [0]*(i+3)
            for j in range(1,i+2):
                line[j] = save[j] + save[j-1]
                print(line[j], end=' ')
            print()
            save = line
        else:
            print(save[1])