from sys import setrecursionlimit
setrecursionlimit(10**6)
N, M = map(int, input().split())
AB = list()
p = []
for i in range(N):
    p.append(p[i][:])
seen = [False]*N
n = [-1]*N
history = []
seen[0] = True
for i in p:
    print(id(p))
exit()
for i in range(M):
    A, B = map(int, input().split())
    p[A-1].append(B-1)
    p[B-1].append(A-1)
print(p)
for i in p:
    print(i)
exit()
#D.F.S
cnt=0
def F(v):
    global cnt
    cnt += 1
    for i in p[v]:
        #print(i)
        n[i]=cnt
        if seen[i]:
            cnt-=1
            continue
        F(i)
F(0)
del n[0]
for i in n:
    print(i)