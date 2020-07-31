s=str(input())
n=0
sign=''
ans=0
tmp=[]
for ch in s:
    if ch=='*':
        sign='*'
    elif ch=='+':
        if sign=='*':
            if 0 not in tmp:
                #print(tmp)
                ans+=1
            
        else:
            if n!=0:
                #print([n])
                ans+=1
        sign='+'
        tmp=[]
    else:
        n=int(ch)
        tmp.append(n)

if 0 not in tmp and len(tmp)>0:
    #print(tmp)
    ans+=1
print(ans)