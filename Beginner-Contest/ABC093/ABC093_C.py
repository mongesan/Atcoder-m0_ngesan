l=list(map(int, input().split()))
l.sort()
cnt=0
while l[0]!=l[1] or l[0]!=l[2] or l[1]!=l[2]:
    l.sort()
    #print(l)
    if l[1] == l[2]:
        l[0] += 2
    else:
        l[0] += 1
        l[1] += 1
    cnt+=1

print(cnt)
