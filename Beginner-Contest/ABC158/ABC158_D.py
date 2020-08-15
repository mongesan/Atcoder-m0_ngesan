s = str(input())
q = int(input())
for i in range(q):
    tmp = tuple(map(str, input().split()))
    if len(tmp) == 3:  # pattern 2
        if int(tmp[1]) == 1:
            s = tmp[2]+s
        else:
            s += tmp[2]
    else:
        s = s[::-1]

print(s)
