n=int(input())
c=str(input())

r=c.count('R')
w=0
ans=r
for ch in c:
    if ch=='W':
        w+=1
    else:
        r-=1
    m=min(r,w)
    ans=min(r+w-m, ans)

print(ans)