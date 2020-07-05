from math import inf
n, m, x = map(int, input().split())
ca = list()
for _ in range(n):
    ca.append(list(map(int, input().split())))

money = inf
tmp = 1
for i in range(n):
    tmp += 2**i
for i in range(tmp):
    B = str(format(i, str(n).zfill(n)+'b'))
    j = 0
    cnt = 0
    a = [0]*m
    for ch in B:
        if ch == '1':
            cnt += ca[j][0]
            for k in range(1, m+1):
                a[k-1] += ca[j][k]
        j += 1
    for ch in a:
        if ch < x:
            break
    else:
        money = min(cnt, money)
print(-1 if money == inf else money)
