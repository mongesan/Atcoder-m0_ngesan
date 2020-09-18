n,m=map(int, input().split())
Fib=[1,2]
x=1
while Fib[x]+Fib[x-1]<=n:
    Fib.append(Fib[x]+Fib[x-1])
    x+=1
p=0
m=1
for _ in range(m):
    a=int(input())
    if a!=1 and a-p==1:
        m*=0
    else:
        m*=Fib[a-p]
    p=a
print(m)
