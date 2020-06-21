n=int(input())
alp=list()
for ch in 'abcdefghijklmnopqrstuvwxyz':
    alp.append(ch)

digit=0
while n>26**(digit+1):
    digit+=1
ans=list()
for d in reversed(range(1,digit+1)):
    for m in reversed(range(1,27)):
        if n>=m*(26**d):
            n-=m*(26**d)
            ans.append(m-1)
            break
ans.append(n-1)
name=str()
for i in ans:
    name+=alp[i]
#print(ans)
print(name)