from collections import Counter
n, k = map(int, input().split())
A = list(map(int, input().split()))
c = Counter(A)
cnt = 0
ans = 0
m = len(c)-k
if m < 0:
    m = 0
for k, v in sorted(c.items(), key=lambda x: x[1]):
    if cnt == m:
        break
    ans += v
    cnt += 1

print(ans)
