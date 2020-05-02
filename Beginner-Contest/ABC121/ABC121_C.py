N, M = map(int, input().split())
AB = list()
for i in range(N):
    AB.append(tuple(map(int, input().split())))
AB.sort()
money = 0
i = 0
while M > AB[i][1]:
    M -= AB[i][1]
    money += AB[i][0]*AB[i][1]
    #print(money)
    i += 1

money += AB[i][0]*M
M = 0
print(money)
