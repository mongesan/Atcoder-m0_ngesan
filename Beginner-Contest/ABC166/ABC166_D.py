X = int(input())
l = list()
i = int()
while i**5-(i-1)**5 <= 10**9:
    l.append(i**5)
    l.append(0-i**5)
    i += 1
for i in range(len(l)):
    for j in range(i, len(l)):
        if abs(l[i]-l[j])==X:
            if l[i]-l[j]==X:
                A=l[i]
                B=l[j]
            else:
                A=l[j]
                B=l[i]
            #print(A,B)
            ifAM=False
            ifBM=False
            if A<0:
                ifAM=True
            if B<0:
                ifBM=True
            A=int(abs(A)**0.2)
            B=int(abs(B)**0.2)
            if ifAM:
                A=0-A
            if ifBM:
                B=0-B
            print(A, B)
            exit()