n=int(input())
c=str(input())
W,R=[],[]
i=0
for ch in c:
    if ch=='W':
        W=[i]+W
    else:
        R.append(i)
    i+=1
ans=int()
print(R,W)
if len(R)!=0 and len(W)!=0:
    while R[0]>W[0]:
        del R[0]
        del W[0]
        ans+=1
        if len(R)==0 or len(W)==0:
            break

print(ans, R,W)