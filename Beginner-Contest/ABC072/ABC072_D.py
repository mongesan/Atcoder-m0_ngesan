n=int(input())
P=list(map(int, input().split()))
ans=0
n=1
for i in P:
    print(i,n)
    if i==n:
        ans+=1
    n+=1
print(ans)
print(ans//2+ans%2)