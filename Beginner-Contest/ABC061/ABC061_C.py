n,k=map(int, input().split())
l=[tuple(map(int, input().split())) for _ in range(n)]
l.sort()
a,b=0,0
for t in l:
    b=a+t[1]
    if a<k<=b:
        print(t[0])
        exit()
    a=b
print(l)