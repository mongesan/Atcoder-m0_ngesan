N = int(input())
a = list(map(int, input().split()))

cnt = 0
ans = 0
while cnt!=3:
    for n in range(N):
        if a[n]%2!=0 or (N!=1 and n):
            cnt+=1
            a[n] *= 3
        else:
            a[n] //= 2
    if cnt!=3:
        ans += 1

print(ans)
