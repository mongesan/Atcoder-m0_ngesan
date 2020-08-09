from scipy.misc import comb
n, m=map(int, input().split())
k,s=[],[]
for _ in range(m):
    tmp=list(map(int, input().split()))
    k.append(tmp[0])
    s.append(tmp[1:])
p=list(map(int, input().split()))

for i in range(m):
    