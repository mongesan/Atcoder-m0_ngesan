n, m, x = map(int, input().split())
l=list()

for i in range(n):
    a=list(map(int, input().split()))
    l.append(a)
ans=10**8
for i in range(2**n):
    bag=list()
    for j in range(n):
        if ((i >> j)) & 1):
            bag.append(l[j])
    skill=[0]*m
    