from collections import Counter
h,w=map(int, input().split())
x,y=map(int, input().split())
x-=1
y-=1
gx,gy=map(int, input().split())
gx-=1
gy-=1
s=[]
for i in range(h):
    tmp=[]
    for ch in str(input()):
        tmp.append(ch)
    s.append(tmp)
m=Counter()
i,j=0,0
for l in s:
    j=0
    for t in l:
        if t=='.':
            m[(i,j)]=0
        else:
            m[(i,j)]=-1
        j+=1
    i+=1
print(m)
print(s)
def BFS(x,y):
    exit()