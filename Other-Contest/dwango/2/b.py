n=int(input())
K=tuple(map(int, input().split()))
l=[]
for i in range(n-2):
    l.append(min(K[i],K[i+1]))
if K[0]==l[0]:
    l=[1]+l
else:
    l=[K[0]]+l
if K[n-2]==l[len(l)-1]:
    l.append(1)
else:
    l.append(K[n-2])

print(*l)