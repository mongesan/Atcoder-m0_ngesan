N, M = map(int, input().split())
sp = 0
ep = 10**5+1
for i in range(M):
    L, R = map(int, input().split())
    sp = max(sp, L)
    ep = min(ep, R)

print(max(0, ep-sp+1))
