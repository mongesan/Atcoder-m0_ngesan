n,m=map(int, input().split())
Fib=[1,2]
for i in range(n-2):
    Fib.append(Fib[i]+Fib[i+1])
ans=1
if m==0:
    ans=Fib[n-1]
else:
    A=[]
    for i in range(m):
        A.append(int(input()))
    #First
    if A[0]!=1:
        ans*=Fib[A[0]-2]
    else:
        ans*=1
    #Locate
    for i in range(1,m):
        if A[i]-A[i-1]!=1:
            ans*=Fib[A[i]-A[i-1]-2]
        else:
            ans*=0
    #Final
    if n-A[m-1]!=1:
        ans*=Fib[n-A[m-1]-2]
    else:
        ans*=1
    print(ans%(10**9+7))
    
        
