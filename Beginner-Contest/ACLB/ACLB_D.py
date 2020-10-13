n,k=map(int, input().split())
a=int(input())
b=a
l=[a]
x=[]
y=[0]
for i in range(n-1):
    tmp=int(input())
    l.append(tmp)
    x.append(tmp-a)
    y.append(tmp-b)
    a=tmp

print(l)
print(x)
print(y)
total=0
ans=0
for i in x:
    total+=i
    if total<=k:
        total=0
        ans+=1
if n==1:
    print(1)
else:
    print(ans)