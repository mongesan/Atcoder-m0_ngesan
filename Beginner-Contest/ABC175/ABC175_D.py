n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
l = []
now=0
for _ in range(n):
    l.append(c[now])
    now=p[now]-1

l=l*2
ans = 0
tmp = 0
for j in range(k):
    now = 0
    for i in range(k % n):
        now += l[j+i]
        tmp = max(tmp, now)
    ans = max(tmp, ans)
print(l)
print(ans+(k//n)*sum(c))
