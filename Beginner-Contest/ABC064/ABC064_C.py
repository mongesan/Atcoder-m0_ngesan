n = int(input())
A = list(map(int, input().split()))
L = [0]*8
tourist = int()
for a in A:
    n = a//400
    if n > 7:
        tourist += 1
    else:
        L[n] = 1

cnt = int()
for l in L:
    if l == 1:
        cnt += 1

if cnt==0:
    print(1,tourist)
else:
    print(cnt, cnt+tourist)