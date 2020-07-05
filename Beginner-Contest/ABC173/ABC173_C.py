def check(S):
    n=0
    for ch in S:
        if ch=='#':
            n+=1
    return n
h,w,k=map(int, input().split())
c=[str(input()) for _ in range(h)]
hl=[]
wl=[]
cnt=0
for s in c:
    tmp=check(s)
    hl.append(tmp)
    cnt+=tmp
for i in range(w):
    s=str()
    for j in range(h):
        s+=c[j][i]
    wl.append(check(s))
n=cnt-k
print(hl, wl, n)
