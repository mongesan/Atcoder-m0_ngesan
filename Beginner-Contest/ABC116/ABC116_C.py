N=int(input())
h=list(map(int, input().split()))
cnt=0
sp=0
while sum(h)!=0:
    for i in range(N):
        if h[i]==0:
            if i-sp!=0:
                cnt+=1
            sp=i+1
            print(h)
        else:
            h[i] -= 1
    if i-sp+1!=0:
        cnt+=1
    print(h)
print(cnt)
