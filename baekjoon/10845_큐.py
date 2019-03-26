def push(num):
    que.append(num)


def pop():
    if que:
        return que.pop(0)
    else:
        return -1


def size():
    return len(que)


def empty():
    if que:
        return 0
    else:
        return 1


def front():
    if que:
        return que[0]
    else:
        return -1


def back():
    if que:
        return que[-1]
    else:
        return -1


N = int(input())
que = []
for _ in range(N):
    cmd = list(input().split())
    if cmd[0] == 'push':
        push(int(cmd[1]))
    elif cmd[0] == 'pop':
        a = pop()
        print(a)
    elif cmd[0] == 'size':
        a = size()
        print(a)
    elif cmd[0] == 'empty':
        a = empty()
        print(a)
    elif cmd[0] == 'front':
        a = front()
        print(a)
    else:
        a = back()
        print(a)