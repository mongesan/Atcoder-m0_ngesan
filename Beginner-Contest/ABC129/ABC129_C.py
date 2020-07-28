n, m=map(int, input().split())
A = [int(input()) for i in range(m)]
Fib = [0,1,2]
for i in range(2,10**5-2):
    Fib.append(Fib[i-1]+Fib[i])
way=1
i=1
j=0
cnt=1
l=[]
A.append(n)
while i<=n:
    if i==A[j]:
        l.append(cnt-1)
        print(cnt-1)
        cnt=0
        j+=1
    i+=1
    cnt+=1
if l[0]==0:
    del l[0]

for i in l:
    way*=Fib[i+1]

print(way%1000000007)