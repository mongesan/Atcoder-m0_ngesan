n = int(input())
A = list(map(int, input().split()))
cnt = 0
i = 1
for a in A:
    if i % 2 == 1 and a % 2 == 1:
        cnt += 1
    i += 1

print(cnt)
