n=int(input())
ans=[int(0)]*6
for _ in range(n):
    h,l=map(float, input().split())
    #High Temp
    if h>=35:
        ans[0]+=1
    elif h>=30:
        ans[1]+=1
    elif h>=25:
        ans[2]+=1
    #Low Temp
    if l>=25:
        ans[3]+=1
    #Other
    if l<0 and h>=0:
        ans[4]+=1
    if h<0:
        ans[5]+=1

for i in range(6):
    ans[i]=str(ans[i])

print(' '.join(ans))