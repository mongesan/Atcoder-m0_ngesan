s=str(input())
q=int(input())
Q=[]
r=0
for i in range(q):
    t,f,c=map(int, input().split())
    if t==1:
        if r==0:
            r+=1
        else:
            r-=1
    else:
        Q.append((f,c))