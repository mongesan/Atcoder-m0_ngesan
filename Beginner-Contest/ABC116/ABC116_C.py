n = int(input())
h = list(map(int, input().split()))
cnt = int()
for i in reversed(range(1, max(h)+1)):
    tmp = list()
    for j in h:
        if i <= j:
            tmp.append(1)
        else:
            tmp.append(0)
    #print(tmp)
    if tmp[0]==1:
        cnt += 1
    for j in range(1, n):
        if tmp[j]-tmp[j-1] == 1:
            cnt += 1

print(cnt)
