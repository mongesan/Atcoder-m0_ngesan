A, B, X = map(int, input().split())
l = 0
r = 1000000001
while l < r-1:
    m = l + (r - l) // 2
    p = m * A + B * len(str(m))
    if p > X:
        r = m
    else:
        l = m

print(l)
