s=str(input())
k=int(input())
cnt=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        s=s[:i+1]+'-'+s[i+2:]
        cnt+=1
if s[0]==s[len(s)-1]:
    cnt+=1
print(cnt*k)