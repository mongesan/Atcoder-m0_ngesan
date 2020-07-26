n, k = map(int, input().split())
R = sorted(list(map(int, input().split())))
n = 0
for r in R[n-k:]:
    n = (n+r)/2
print(n)
