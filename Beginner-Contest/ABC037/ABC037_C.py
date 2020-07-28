n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [n-k+1]*n
ans = int()
for i in range(n-k):
    b[i] -= n-k-i
    b[n-1-i] -= n-k-i

for i in range(n):
    ans += a[i]*b[i]

print(ans)
