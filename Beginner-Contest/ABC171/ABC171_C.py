n=int(input())
alp=list()
for ch in '-abcdefghijklmnopqrstuvwxyz':
    alp.append(ch)

m=0
while n>26**(m+1):
    m+=1
    #print('inf')
    #print(n, 26**(m+1))
m+=1
k=[]
for i in reversed(range(m+1)):
    if i==0:
        x=n
    else:
        x=n//(26**i)
    if x==0:
        if i==0 or i!=m:
            k.append(1)
    else:
        k.append(x)
    #print(x,i)
    #print(x*26**i)
    n-=x*26**i
s=str()
for i in k:
    s+=alp[i]

print(s)