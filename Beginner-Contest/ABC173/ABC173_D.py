from collections import Counter
n=int(input())
s=str(input())
R,G,B=[],[],[]
i=0
for ch in s:
    if ch=='R':
        R.append(i)
    elif ch=='G':
        G.append(i)
    else:
        B.append(i)
    i+=1
lr,lg,lb=len(R),len(G),len(B)
B=Counter(B)
ans=lr*lg*lb
for i in R:
    for j in G:
        if B[j+j-i]>=1 or i>j or 1>j+j-i>n or 1>i>n or 1>j>n:
            print(i,j,j+j-i)
            ans-=1

print(ans)