n=int(input())
l=list(map(int, input().split()))
l.sort()
print(l)
#a<b<c
def Nibutan(L,R):
    global l,a,b
    if L==R:
        return(l[L])
    if l[R]<a+b:
        return(Nibutan((L+R)//2,R))
    else:
        return(Nibutan(L,(L+R)//2))
for i in range(n-1):
    a=l[i]
    for j in range(i+1,n-1):
        b=l[j]
        #2butan
        print(a,b,Nibutan(j,n-1))