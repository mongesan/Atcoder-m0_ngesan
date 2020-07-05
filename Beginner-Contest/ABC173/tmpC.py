from copy import deepcopy
def check(S):
    n=0
    for ch in S:
        if ch=='#':
            n+=1
    return n
h,w,k=map(int, input().split())
tmp=[list(input()) for _ in range(h)]
c=deepcopy(tmp)

y=0
for l in c:
    x=check(''.join(l))
    y+=x

n=0
for i in range(h+w):
    n+=2**i
n+=1
m=0
for i in range(n):
    i=format(i, str(h+w).zfill(2)+'b')
    H=i[:h]
    W=i[h:]
    ans=0
    x=0
    for j in H:
        if j=='1':
            ans+=check(''.join(c[x]))
            #print(''.join(c[x]))
            c[x]=['.']*w
        x+=1
    x=0
    for j in W:
        if j=='1':
            s=str()
            for z in range(h):
                s+=c[z][x]
            ans+=check(s)
            for z in range(h):
                c[z][x]='.'
        x+=1
    #print(H,W,y-ans,k)
    if k==y-ans:
        m+=1
    c=deepcopy(tmp)

print(m)