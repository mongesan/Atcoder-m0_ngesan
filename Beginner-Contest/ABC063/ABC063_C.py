n = int(input())
S = list()
for _ in range(n):
    S.append(int(input()))
point = sum(S)
if point % 10 == 0:
    S.sort()
    for s in S:
        if s % 10 != 0:
            point -= s
            break
    else:
        point = 0
print(point)
