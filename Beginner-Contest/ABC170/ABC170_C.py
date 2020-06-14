x,n=map(int, input().split())
P=list(map(int, input().split()))
ans=[]
for i in range(102):
    ans.append(i)

m=99999999999999
for p in P:
    del ans[ans.index(p)]
y=99999999999999
#print(ans)
for i in ans:
    if abs(i-x)<y:
        y=abs(i-x)
        m=i

print(m)