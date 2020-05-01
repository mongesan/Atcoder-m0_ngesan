from math import sqrt


def route(a, b):
    return(sqrt((p[a-1][0]-p[b-1][0])**2+(p[a-1][1]-p[b-1][1])**2))


n = int(input())
p = list()
for i in range(n):
    p.append(tuple(map(int, input().split())))

sum = int()
cnt = int()
for i in range(1, n):
    for j in range(i+1, n+1):
        #print(i, j)
        sum += route(i, j)
        cnt += 1

sum *= n-1
print(sum/cnt)
