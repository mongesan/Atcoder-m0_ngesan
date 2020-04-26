a, b, c, d = map(int, input().split())
cnt = 0
while a > 0 and c > 0:
    if cnt % 2 == 0:
        c -= b
    else:
        a -= d
    cnt += 1
print('Yes' if c <= 0 else 'No')
