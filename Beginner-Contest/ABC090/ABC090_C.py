n, m = map(int, input().split())
if n > 2:
    n -= 2
elif n == 2:
    n = 0
if m > 2:
    m -= 2
elif m == 2:
    m = 0
print(n*m)
