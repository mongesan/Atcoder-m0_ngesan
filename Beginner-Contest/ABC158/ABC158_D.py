s = str(input())
q = int(input())
for i in range(q):
    query = list(map(str, input().split()))
    query[0]=int(query[0])
    if len(query)!=1:
        query[1]=int(query[1])
    if query[0] == 1:
        if len(s) != 1:
            s = s[len(s)-1]+s[1:len(s)-1]+s[0]
    else:
        if query[1] == 1:
            s = query[2] + s
        else:
            s += query[2]

print(s)
