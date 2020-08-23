n=str(input())
ans=0
for ch in n:
    ans+=int(ch)
if ans%9==0:
    print('Yes')
else:
    print('No')