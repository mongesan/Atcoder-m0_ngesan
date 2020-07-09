from itertools import combinations
l=list(map(int, input().split()))
c=list(combinations(l, 3))
n=list()
for x in c:
    n.append(sum(x))

print(sorted(n)[len(n)-3])