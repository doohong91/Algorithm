date = [0,31,28,31,30,31,30,31,31,30,31,30]
days = ['SUN','MON','TUE','WED','THU','FRI','SAT']

a,b = [int(i) for i in input().split()]
print(days[(sum(date[:a]) + b) % 7])