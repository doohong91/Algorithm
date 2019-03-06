def push(num):
    stack.append(num)

def pop():
    try: 
        a = stack.pop()
        return a
    except: return -1

def size():
    return len(stack)

def empty():
    if stack: return 0
    else: return 1

def top():
    if not stack: return -1
    else: return stack[-1]

N = int(input())
stack = []
result = []
for n in range(N):
    command = list(input().split())
    if len(command) == 2:
        push(int(command[1]))
    elif command[0] == 'pop':
        result.append(pop())
    elif command[0] == 'size':
        result.append(size())
    elif command[0] == 'empty':
        result.append(empty())
    elif command[0] == 'top':
        result.append(top())
for r in result:
    print(r)