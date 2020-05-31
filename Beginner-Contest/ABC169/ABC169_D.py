import collections
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

N=int(input())
l = prime_factorize(N)
m = collections.Counter([])
m[1]=1
x=1
cnt=0
y=list()
for i in range(len(l)):
    if x!=1 and x%l[i]!=0:
        x=1
    x*=l[i]
    #print(x)
    if m[x]==0:
        y.append(x)
        m[x]=1
        cnt+=1
        x=1
#print(l)
#print(m)
#print(x,y)
print(cnt)
