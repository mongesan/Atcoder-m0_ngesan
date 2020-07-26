from itertools import combinations
n, m=map(int, input().split())
l=list()
for _ in range(n):
    l.append([])

for _ in range(m):
    a,b=map(int, input().split())
    l[a-1].append(b-1)
    l[b-1].append(a-1)

f=list()
for fs in l:
    if len(fs)>=2:
        for c in list(combinations(fs, 2)):
            f.append(c)

ans=[0]*n
for c in f:
    ans[c[0]]+=1
    ans[c[1]]+=1

for s in ans:
    print(s)