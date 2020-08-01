N=int(input())
*V,=map(int,input().split())

from collections import*
C1=Counter(V[::2]).most_common()+[(0,0)]
C2=Counter(V[1::2]).most_common()+[(0,0)]

K1=C1[0][0]
V1=C1[0][1]
K2=C2[0][0]
V2=C2[0][1]
if K1==K2:
    if V1>V2:
        V2=C2[1][1]
    elif V2>V1:
        V1=C[1][1]
    else:
        V2=max(C1[1][1],C2[1][1])

print(N-V1-V2)
