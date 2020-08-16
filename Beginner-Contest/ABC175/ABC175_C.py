x,k,d=map(int, input().split())
x=abs(x)
k=abs(k)
d=abs(d)
ans=[]
if x<k*d:
    div=x//d
    if (k-div)%2==0:
        ans.append(abs(x-d*(div)))
    else:
        ans.append(abs(x-d*(div+1)))
    #ans.append(abs(x-d*(div+1)))
else:
    ans.append(x-k*d)

print(min(ans))