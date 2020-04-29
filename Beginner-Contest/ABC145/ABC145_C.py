from itertools import permutations
from math import sqrt
N = int(input())
pos = list()
for _ in range(N):
    pos.append(tuple(map(int, input().split())))

dist = list()
for i in range(1,N):
    dist.append(sqrt((pos[i-1][0]-pos[i][0])**2+(pos[i-1][1]-pos[i][1])**2))

print(sum(dist)/len(dist))