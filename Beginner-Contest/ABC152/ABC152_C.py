n = int(input())
p = list(map(int, input().split()))

cnt = 1
for i in range(1, n):
    if p[i-1] >= p[i]:
        cnt += 1
    else:
        p[i] = p[i-1]
print(cnt)
