n=int(input())
l=[tuple(map(int, input().split())) for i in range(n)]
l.sort(key=lambda x:x[1])
cnt=0
for t in l:
    cnt+=t[0]
    if cnt>t[1]:
        print('No')
        exit()

print('Yes')