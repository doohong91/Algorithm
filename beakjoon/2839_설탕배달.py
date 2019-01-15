# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 
# 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

sugar = int(input())
li = [i + (sugar - 5*i)//3 for i in range((sugar//5)+1) if (sugar - 5*i)%3 == 0]
if li:
    print(min(li))
else:
    print(-1)  