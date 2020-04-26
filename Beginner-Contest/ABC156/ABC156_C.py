n = int(input())
l = list(map(int, input().split()))
m = 10**10
for p in range(1, max(l)+1):
    tmp = 0
    for x in l:
        tmp += (x-p)**2
    m = min(m, tmp)

print(m)
