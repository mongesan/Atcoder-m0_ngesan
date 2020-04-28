#from math import factorial
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
l = set()

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            l.add((i, j, k))
l = list(l)
l.sort()
print(l)
print(l.index(tuple(p))-l.index(tuple(q)))
