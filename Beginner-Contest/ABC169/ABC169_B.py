n=int(input())
l=list(map(int, input().split()))
m=1
for i in range(n):
    m*=l[i]
    if m>10**18:
        if 0 in l:
            print(0)
            exit()
        print(-1)
        exit()

print(m)