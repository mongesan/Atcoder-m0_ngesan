N, K = map(int, input().split())
h = list()
for i in range(N):
    h.append(int(input()))
h.sort()
ans = 10**9+1
for i in range(N-1):
    ans = min(ans, abs(h[i]-h[i+1]))

print(ans)