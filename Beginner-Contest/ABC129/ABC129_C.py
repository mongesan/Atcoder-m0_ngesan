n,m=map(int, input().split())
FIB=[0,2]
x=1
for i in range(n):
    FIB.append(FIB[x-1]+FIB[x])
    x+=1
FIB[0]=0
print(FIB)
sp=0
ans=1
a=[0]
for _ in range(m):
    a.append(int(input()))
a.append(n)
print(a)
for i in range(1,len(a)):
    y=a[i]-a[i-1]-2
    if i==1 and y==1:
        ans*=1
    else:
        print(FIB[y])