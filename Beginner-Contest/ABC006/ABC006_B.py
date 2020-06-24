n=int(input())
tri=[0,0,1]
for i in range(n-3):
    ans = (tri[i]+tri[i+1]+tri[i+2])%10007
    tri.append(ans)
if n==1 or n==2 or n==3:
    ans = tri[n-1]
print(ans)
