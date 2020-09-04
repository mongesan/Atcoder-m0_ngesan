from collections import Counter
import collections
n, m = map(int, input().split())
x = [-1 for _ in range(n)]  # -1
g = []
for i in range(m):
    a, b = map(int, input().split())
    # if mouyatta[tuple(sorted([a,b]))]==0:
    # mouyatta[tuple(sorted([a,b]))]+=1
    if x[a-1]+x[b-1]==0
        continue
    elif koseki[a-1] != -1:
        koseki[b-1] = koseki[a-1]
        group[koseki[a-1]] += 1
    elif koseki[b-1] != -1:
        koseki[a-1] = koseki[b-1]
        group[koseki[b-1]] += 1
    else:
        group.append(2)
        koseki[a-1] = len(group)-1
        koseki[b-1] = len(group)-1
# print(group)
print(max(group))
