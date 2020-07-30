S=str(input())
n=0
ch=S[0]
for s in S:
    if ch!=s:
        n+=1
    ch=s
print(n)