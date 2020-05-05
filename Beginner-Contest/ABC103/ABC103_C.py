N=int(input())
a=list(map(int, input().split()))

ans = 0
m = 1
for i in range(N):
    m *= a[i]

m-=1
for A in a:
    ans += m % A

print(ans)