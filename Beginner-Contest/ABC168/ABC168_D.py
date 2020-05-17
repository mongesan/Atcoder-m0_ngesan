N, M = map(int, input().split())
AB=list()
p=[[]]*N
seen=[False]*N
history=[]
seen[0]=True
for i in range(M):
    A, B=map(int, input().split())
    p[A-1].append(B-1)
    p[B-1].append(A-1)

for i in range(N):
    p[i]=list(set(p[i]))

def dfs(n):
    for i in range(n):
        seen[]
    seen[]


#DFS! DFS!

