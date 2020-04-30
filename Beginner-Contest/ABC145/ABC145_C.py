from itertools import permutations
from math import sqrt
N = int(input())
pos = list()
r = list()
for _ in range(N):
    pos.append(tuple(map(int, input().split())))
for v in permutations(range(N), N):
    r.append(v)

print(r)
dist = list()
for i in range(len(r)-1):
    s
    dist.append(sqrt((pos[i][0]-pos[i+1][0]) **
                         2+(pos[i][1]-pos[i+1][1])**2))

print(sum(dist)/len(dist))
